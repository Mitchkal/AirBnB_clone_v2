#!/usr/bin/python3
"""
module 1-pack_web_static
"""


import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    generates a tgz archiveof web_static folder
    """

    local("mkdir -p versions")

    now = datetime.now()
    date_str = now.strftime("%Y%m%d%H%M%S")

    archive_name = "web_static_{}.tgz".format(date_str)

    result = local("tar -cvzf versions/{} web_static".format(
        archive_name))

    if result.succeeded:
        archive_path = os.path.join("versions", archive_name)
        # local("chmod 664 {}".format(archive_path))
        print("web_static packed: {} -> {} Bytes".format(
            archive_path, os.path.getsize(archive_path)))
        return archive_path
    else:
        return None
