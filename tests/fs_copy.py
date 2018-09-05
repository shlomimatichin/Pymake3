#!/usr/bin/python3

#---------------------------------------
# IMPORTS
#---------------------------------------

import os

import test

from pymake3 import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

SRCDIR  = 'files'
DESTDIR = 'files2'

#---------------------------------------
# SCRIPT
#---------------------------------------

test.true(os.path.exists(SRCDIR), "test files missing")
test.false(os.path.exists(DESTDIR), "temp dir should not exist yet")

# The directory will be removed by the fs_find_files test.
test.equal(copy(SRCDIR, DESTDIR, '*.txt'), 3, "wrong number of files copied")

test.success()
