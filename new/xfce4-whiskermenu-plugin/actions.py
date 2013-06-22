#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure()
    
def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.domo("po/xfce4-whiskermenu-plugin.po", "tr", "xfce4-whiskermenu-plugin.mo")
    
    pisitools.dodoc("COPYING")