#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009,2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools, pisitools, shelltools

shelltools.export("JAVAC","/opt/sun-jdk/bin/javac")

def build():
    autotools.make("Build")

def install():
    pisitools.insinto("/usr/bin/", "Bin/J7Z.sh")
    pisitools.insinto("/usr/share/J7Z/Desktop", "Desktop/*")
    pisitools.insinto("/usr/share/J7Z/Lib", "Lib")
    pisitools.insinto("/usr/share/doc/j7z", "License/*")
    pisitools.insinto("/usr/share/J7Z/Dist/", "Dist/J7Z.jar")
    pisitools.insinto("/usr/share/J7Z/License/", "License/*")
    pisitools.insinto("/usr/share/J7Z/Lists/", "Lists/")
    pisitools.insinto("/usr/share/J7Z/Profiles/", "Profiles/*")
    pisitools.insinto("/usr/share/applications/", "Desktop/Menu/J7Z.desktop")
    pisitools.insinto("/usr/share/icons/hicolor/16x16/actions/", "Source/Image/actions/ark_addfile.png")
    pisitools.insinto("/usr/share/icons/hicolor/32x32/apps/", "Source/Image/apps/J7Z.png")
    pisitools.insinto("/usr/share/pixmaps", "Source/Image/apps/J7Z.png")