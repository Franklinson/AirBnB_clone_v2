#!/usr/bin/env python3
from fabric.api import env, run, put, local
from datetime import datetime
from os.path import exists

# Define the remote servers
env.hosts = ['100.26.167.23', '34.203.38.116']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """
    Create a compressed archive of the web_static folder.
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        local("tar -czvf versions/\
web_static_{}.tgz web_static".format(timestamp))
        return "versions/web_static_{}.tgz".format(timestamp)
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Deploy the archive to the web servers.
    """
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        release_dir = "/data/web_static/\
releases/{}".format(archive_name.split(".")[0])
        current_dir = "/data/web_static/current"

        # Upload archive
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(release_dir))

        # Uncompress archive
        run("tar -xzf /tmp/{} -C {}".format(archive_name, release_dir))

        # Create symbolic link
        run("rm -rf {}".format(current_dir))
        run("ln -s {} {}".format(release_dir, current_dir))

        # Clean up
        run("rm /tmp/{}".format(archive_name))
        return True

    except Exception as e:
        return False


def deploy():
    """
    Deploy the latest version of the web_static folder.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)
