#!/usr/bin/python3
# creates and distributes archive to web server

import os
from os.path import exists, basename
from datetime import datetime
from fabric.api import local, run, put, sudo, env

env.hosts = ['100.25.145.4', '52.91.152.172']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """
    generates a tgz archiveof web_static folder
    """

    local("mkdir -p versions")

    now = datetime.now()
    date_str = now.strftime("%Y%m%d%H%M%S")

    archive_name = "web_static_{}.tgz".format(date_str)

    local("tar -cvzf versions/{} web_static".format(
        archive_name))

    # if result.succeeded:
    archive_path = os.path.join("versions", archive_name)
        # local("chmod 664 {}".format(archive_path))
    print("web_static packed: {} -> {} Bytes".format(
        archive_path, os.path.getsize(archive_path)))

    return archive_path
    # else:
        # return None


def do_deploy(archive_path):
    """
    deploys a compressed web static folder to remote servers
    """
    if not exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp')

        filename = basename(archive_path)
        folder_name = filename.split('.')[0]
        # local('echo "filename is {}"'.format(filename))
        # local('echo "folder name is {}"'.format(folder_name))

        run("mkdir -p /data/web_static/releases/{}/".format(folder_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            filename, folder_name))

        run("rm /tmp/{}".format(filename))
        run("rm -rf /data/web_static/current")
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static\
/releases/{}".format(folder_name, folder_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(
            folder_name))

        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(folder_name))
        print('New version deployed!')
        return True

    except Exception as e:
        print('Deployment failed: {}'.format(e))
        return False


def deploy():
    """
    deploys archive to web server
    """

    archive_path = do_pack()

    if archive_path is None:
        return False

    return_val = do_deploy(archive_path)
    return return_val
