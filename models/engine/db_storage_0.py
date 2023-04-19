"""Defines DBStorage class"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instance method"""
        user = os.environ['HBNB_MYSQL_USER']
        password = os.environ['HBNB_MYSQL_PWD']
        host = os.environ['HBNB_MYSQL_HOST']
        db_name = os.environ['HBNB_MYSQL_DB']
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      user, password, host,
                                      db_name), pool_pre_ping=True)
        env = os.environ['HBNB_ENV']
        if env == 'test':
            metadata = MetaData()
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects depending of the class name"""
        Session = sessionmaker(bind=engine)
        self.__session = Session()
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            objs = self.__session.query(cls).all()
        return {"{}.{}".format(obj.__class__.__name__,
                               obj.id): obj for obj in objs}

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj):
        """Delete from the current database session obj if not None"""
        self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and database session"""
        Base.metadata.create_all(engine)
        new_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(new_session)
        self.__session = Session()
