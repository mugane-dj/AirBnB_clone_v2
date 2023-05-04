#!/usr/bin/python3
"""
Fabfile to:
    - generate a .tgz archive from the contents of the web_static folder
"""

from fabric import *
from datetime import datetime


def do_pack():
    """Generate .tgz archive"""
    sudo("mkdir -p versions")
    _datetime = datetime.now()
    archive = "web_static_" + _datetime.strftime("%Y%m%d%H%M%S") + ".tgz"
    result = local("tar -cvzf versions/{} web_static".format(archive))
    if result.return_code == 0:
        return "versions/" + archive
    else:
        return None
