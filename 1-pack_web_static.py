#!/usr/bin/python3
from fabric.api import local, env
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
      Path to the archive if it was created successfully, None otherwise.
    """

    versions_dir = 'versions'
    if not os.path.exists(versions_dir):
        os.makedirs(versions_dir)

    now = datetime.now()

    archive_name = 'web_static_{}{}{}{}{}{}.tgz'.format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)

    archive_path = os.path.join(versions_dir, archive_name)
    local('tar -cvzf {} web_static'.format(archive_path))

    return archive_path
