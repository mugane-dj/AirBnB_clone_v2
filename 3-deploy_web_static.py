#!/usr/bin/python3
"""
Fabfile to:
    - create and distribute an archive to specified web servers
"""
import os
from datetime import datetime
from fabric.api import *


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


env.hosts = [
    '18.234.193.103',
    '100.25.102.172'
]


def do_deploy(archive_path):
    """Uploads we_static to servers"""
    if os.path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            path = "/tmp/{}".format(archive_path.split("/")[-1])
            run("tar -xvzf {} -C /data/web_static/releases/".format(path))
            with cd("/tmp"):
                run("rm -rf {}".format(path))
            run("rm /data/web_static/current")
            link = "/data/web_static/current"
            run("ln -sf {} /data/web_static/releases".format(link))
            return True
        except Exception:
            return False
    else:
        return False


def deploy():
    """Deploys a new release to the specified web servers"""
    try:
        archive_path = do_pack()
    except Exception:
        return False
    try:
        output = do_deploy(archive_path)
        return output
    except Exception as error:
        return error
