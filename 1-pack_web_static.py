from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Create a .tgz archive from the contents of the web_static folder.
    """
    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Create the archive filename using the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Compress the web_static folder into the archive
    result = local("tar -czvf versions/{} web_static".format(archive_name))

    if result.succeeded:
        # Return the path to the generated archive
        return "versions/{}".format(archive_name)
    else:
        return None
