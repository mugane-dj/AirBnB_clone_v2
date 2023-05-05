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
