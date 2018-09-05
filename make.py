#!/usr/bin/python3

#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import py_compile
import sys
import zipfile

sys.path.insert(0, 'src')

from pymake3 import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

CONF={ 'bindir': 'bin',
       'objdir': 'obj',
       'srcdir': 'src',
       'builddir': 'src/build',
       'distdir': 'src/dist',
       'egginfodir': 'src/pymake3.egg-info',
       'target': 'pymake3' }

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@default_target(conf=CONF, desc="builds the pymake3 egg package")
def build(conf):
    os.chdir(conf.srcdir)
    run_program('python3', args=['setup.py', 'bdist_egg'])

@target(conf=CONF, desc="cleans pymake3 by deleting the bin and obj "
                        "directories, as well as removing all .pyc-files")
def clean(conf):
    for s in [conf.builddir, conf.distdir, conf.egginfodir]:
        delete_dir(s)
    for s in find_files(conf.srcdir, '__pycache__'):
        delete_dir(s)

#---------------------------------------
# SCRIPT
#---------------------------------------

pymake3()
