#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system("qmake Qlix.pro")

def build():
    autotools.make()

def install():
    pisitools.dobin("qlix")
    pisitools.doman("qlix.1")
    pisitools.insinto("/usr/share/pixmaps/", "pixmaps/qlix.xpm")
    
    pisitools.dodoc("ChangeLog", "COPYING")