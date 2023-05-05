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
    if os.path.isfile(archive_path):
        try:
            file_name_ext = archive_path.split("/")[-1]
            file_name = file_name_ext.split(".")[0]

            path_ext = "/tmp/{}".format(file_name_ext)
            path = "/data/web_static/releases/{}/".format(file_name)

            put(archive_path, "/tmp/")
            run("mkdir -p {}".format(path))
            run("tar -xzf {} -C {}".format(path_ext, path))
            run("rm -rf {}".format(path_ext))
            run("mv {}/web_static/* {}".format(path, path))
            run("rm -rf {}/web_static".format(path))
            run("rm -rf /data/web_static/current")
            run("ln -s {} /data/web_static/current".format(path))
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
