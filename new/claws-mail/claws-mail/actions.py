#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dosym("/usr/share/icons/hicolor/48x48/apps/claws-mail.png", "/usr/share/pixmaps/claws-mail.png")

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog*", "COPYING", "NEWS", "README", "RELEASE_NOTES", "TODO")