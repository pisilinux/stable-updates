# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pisitools.dosed("Makefile", "/usr/share/games/", "/usr/share/")
    pisitools.dosed("Makefile", "/usr/games", "/usr/bin")
    autotools.make()

def install():    
    pisitools.insinto("/usr/bin/", "fairymax")
    pisitools.insinto("/usr/bin/", "maxqi")
    pisitools.insinto("/usr/bin/", "shamax")
    pisitools.insinto("/usr/share/fairymax/", "data/*")
    
    pisitools.dodoc("copyright", "changelog", "README")