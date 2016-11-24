#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import subprocess

import test

from pymake import *

#---------------------------------------
# SCRIPT
#---------------------------------------

# Some examples require Windows and such, so don't run them on Travis CI.
if 'TRAVIS' in os.environ:
    println('skipping - not compatible with Travis CI')
    test.success()

cwd = os.getcwd()
for s in find_files(os.path.join('..', 'examples'), '*make.py'):
    path, filename = os.path.split(s)

    os.chdir(os.path.join(cwd, path))
    r = subprocess.call(['python', filename])

    if r != 0:
        test.fail("example is broken: " + s)

test.success()
