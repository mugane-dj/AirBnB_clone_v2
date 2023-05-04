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
        archive = "web_static_" + _datetime.strftime("%Y%m%d%H%M%S") + ".tgz"
        local("tar -cvzf versions/{} web_static/".format(archive))
        return "versions/" + archive
    except Exception:
        return None
