#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    pisitools.insinto("/opt/idea", "idea-IU-171.3780.107/*")
    pisitools.dosym("/opt/idea/bin/idea.sh", "/usr/bin/idea")
