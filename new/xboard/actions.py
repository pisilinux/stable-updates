# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile.am", "/games/xboard/", "/xboard/")
    pisitools.dosed("Makefile.in", "/games/xboard/", "/xboard/")
    autotools.configure("--sysconfdir=/etc \
                         --prefix=/usr \
                         --bindir=/usr/bin \
                         --enable-silent-rules \
                         --enable-zippy \
                         --disable-update-mimedb")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.insinto("/usr/share/pixmaps/", "xboard.png")
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "COPYRIGHT", "NEWS", "README", "TODO")