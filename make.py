#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import py_compile
import sys
import zipfile

sys.path.insert(0, 'src')

from pymake import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

CONF={ 'bindir': 'bin',
       'objdir': 'obj',
       'srcdir': 'src',
       'target': 'pymake' }

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target(conf=CONF)
def clean(conf):
    delete_dir(conf.bindir)
    delete_dir(conf.objdir)

    for s in find_files(conf.srcdir, '*.pyc'):
        delete_file(s)

@default_target(conf=CONF)
def build(conf):
    args = find_files(conf.srcdir, '*.py')
    py_compile.main(args)

    copy(conf.srcdir, conf.objdir, '*.pyc')

    create_dir(conf.bindir)

    path = os.path.join(conf.bindir, conf.target)
    zipf = zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED)

    os.chdir(conf.objdir)
    for s in find_files('.'):
        zipf.write(s)

    zipf.close()

#---------------------------------------
# SCRIPT
#---------------------------------------

pymake()
