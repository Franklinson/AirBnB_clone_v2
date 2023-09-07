#!/usr/bin/python3

from fabric.api import env, put, run, sudo
import os

# Define the target web servers.
env.hosts = ['100.26.167.23', '34.203.38.116']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.

    Args:
        archive_path (str): Path to the archive to deploy.

    Returns:
        bool: True if deployment was successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory on the server.
        put(archive_path, '/tmp/')

        # Get the filename without extension.
        archive_filename = os.path.basename(archive_path)
        archive_name_noext = os.path.splitext(archive_filename)[0]

        # Create the release directory.
        release_dir = '/data/web_static/releases/{}'.format(archive_name_noext)
        run('mkdir -p {}'.format(release_dir))

        # Uncompress the archive to the release directory.
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_dir))

        # Remove the archive from the server.
        run('rm /tmp/{}'.format(archive_filename))

        # Remove the old symbolic link.
        old_link = '/data/web_static/current'
        run('rm -f {}'.format(old_link))

        # Create a new symbolic link to the new version.
        new_link = '/data/web_static/current'
        run('ln -s {} {}'.format(release_dir, new_link))

        print("New version deployed!")

        return True
    except Exception as e:
        print("Deployment failed:", str(e))
        return False
