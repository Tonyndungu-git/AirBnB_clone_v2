#!/usr/bin/python3
"""
 generates a .tgz archive from the contents
of the web_static folder
and deploy it to web servers
"""

from datetime import datetime
from fabric.api import local, put, run, env
import os.path

env.hosts = ['35.175.104.197', '100.25.181.13']


def do_deploy(archive_path):
    """
        deploy archive to web servers
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        arch_name = archive_path.split('/')[1]
        arch_name_nex = arch_name.split(".")[0]
        re_path = "/data/web_static/releases/"
        up_path = '/tmp/'
        put(archive_path, up_path)
        run('mkdir -p {}{}/'.format(repath, arch_name_nex))
        run('tar -xzf /tmp/{} -C {}{}/'.format(arch_name, re_path, arch_name_nex))
        run('rm /tmp/{}'.format(arch_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(repath, arch_name_nex))
        run('rm -rf {}{}/web_static'.format(repath, arch_name_nex))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, arch_name_nex))
        return True
    except:
        return False
