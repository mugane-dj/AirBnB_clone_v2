#!/usr/bin/python3
"""
Fabfile to:
    - Distributes an archive to specified web servers.
"""


import os
from fabric.api import env, put, cd, run


env.hosts = [
    '18.234.193.103',
    '100.25.102.172'
]


def do_deploy(archive_path):
    """Uploads we_static to servers"""
    if os.path.isfile(archive_path):
        file_name_ext = archive_path.split("/")[-1]
        file_name = file_name_ext.split(".")[0]

        path_ext = "/tmp/{}".format(file_name_ext)
        path = "/data/web_static/releases/{}/".format(file_name)
        sym_link = "/data/web_static/current"
        if put(archive_path, "/tmp/").failed is True:
            return False
        if run("rm -rf {}".format(path)).failed is True:
            return False
        if run("mkdir -p {}".format(path)).failed is True:
            return False
        if run("tar -xzf {} -C {}".format(path_ext, path)).failed is True:
            return False
        if run("rm -rf {}".format(path_ext)).failed is True:
            return False
        if run("mv {}web_static/* {}".format(path, path)).failed is True:
            return False
        if run("rm -rf {}/web_static".format(path)).failed is True:
            return False
        if run("rm -rf /data/web_static/current").failed is True:
            return False
        if run("ln -s {} {}".format(path, sym_link)).failed is True:
            return False
        return True
    else:
        return False
