#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools


def install():
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "ca/*.po")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "ca/*.mo")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/themes/", "ca/themes/*")
    
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "de_DE/*.po")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "de_DE/*.mo")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/themes/", "de_DE/themes/*")
    
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "es_ES/*.po")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "es_ES/*.mo")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/themes/", "es_ES/themes/*")
    
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "fr_FR/*.po")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "fr_FR/*.mo")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/themes/", "fr_FR/themes/*")
    
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "hu_HU/*.po")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "hu_HU/*.mo")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/themes/", "hu_HU/themes/*")
    
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "it_IT/*.po")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "it_IT/*.mo")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/themes/", "it_IT/themes/*")
    
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "nl_NL/*.po")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "nl_NL/*.mo")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/themes/", "nl_NL/themes/*")
    
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "pl_PL/*.mo")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "pl_PL/*.po")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/themes/", "pl_PL/themes/*")
    
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "pt_BR/*.po")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "pt_BR/*.mo")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/themes/", "pt_BR/themes/*")
    
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "ru_RU/*.po")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "ru_RU/*.mo")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/themes/", "ru_RU/themes/*")
    
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "sv_SV/*.po")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "sv_SV/*.mo")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/themes/", "sv_SV/themes/*")
    
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "tr_TR/*.po")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "tr_TR/*.mo")
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/themes/", "tr_TR/themes/*")
    
    pisitools.insinto("/usr/share/wordpress/wp-content/languages/", "uk/*")
    #pisitools.insinto("/usr/share/wordpress/wp-content/languages/themes/", "uk/themes/*")
