#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import py_compile
import sys
import zipfile

sys.path.insert(0, 'src')

from pymake2 import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

CONF={ 'bindir': 'bin',
       'objdir': 'obj',
       'srcdir': 'src',
       'target': 'pymake2' }

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@default_target(conf=CONF, desc="builds the pymake2 zip package")
@depends_on('compile')
def build(conf):
    create_dir(conf.bindir)

    path = os.path.join(conf.bindir, conf.target)
    zipf = zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED)

    os.chdir(conf.objdir)
    for s in find_files('.'):
        zipf.write(s)

    zipf.close()

@target(conf=CONF, desc="cleans pymake2 by deleting the bin and obj "
                        "directories, as well as removing all .pyc-files")
def clean(conf):
    delete_dir(conf.bindir)
    delete_dir(conf.objdir)

    for s in find_files(conf.srcdir, '*.pyc'):
        delete_file(s)

@target(conf=CONF, desc="compiles pymake2 into the obj directory")
def compile(conf):
    args = find_files(conf.srcdir, '*.py')
    py_compile.main(args)

    copy(conf.srcdir, conf.objdir, '*.pyc')

#---------------------------------------
# SCRIPT
#---------------------------------------

pymake2()
