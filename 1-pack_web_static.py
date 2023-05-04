#!/usr/bin/python3
"""
Fabfile to:
    - generate a .tgz archive from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generate .tgz archive"""
    try:
        local("mkdir -p versions")
        _datetime = datetime.now()
        archive = "versions/web_static_" + _datetime.strftime("%Y%m%d%H%M%S") + ".tgz"
        result = local("tar -cvzf {} web_static/".format(archive))
        return archive
    except:
        return None
