#!/usr/bin/python3
"""
This is a fabric script that generates a .tgz/tar.gz (tar gzip) archive
"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ["35.196.126.34", "35.227.96.120"]
env.user = "ubuntu"


def do_pack():
    """
        This will return the archive path if the archive has been correctly
        gernerated.
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """
        This will distribute an archive to our web servers.
    """
    if os.path.exists(archive_path) is False:
        return False
    archived_file = archive_path.split("/")[1]
    archived_file_no_ext = archived_file.split(".")[0]
    newest_version = "/data/web_static/releases/" + archived_file_no_ext

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -zxf /tmp/{} -C {}/".format(archived_file,
                                                  newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    except Exception:
        return False
