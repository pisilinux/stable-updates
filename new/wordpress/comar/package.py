#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.mkdir("/usr/share/wordpress/wp-content/uploads")
    os.system("/bin/chmod -R 0755 /usr/share/wordpress/wp-content/uploads")
    os.system("/bin/chown -R apache:apache /usr/share/wordpress/wp-content/uploads")