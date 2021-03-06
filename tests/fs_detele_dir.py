#!/usr/bin/python3

#---------------------------------------
# IMPORTS
#---------------------------------------

from os import path

import test

from pymake3 import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

# Directory is created by the func_create_dir test.
PATH = 'tempdir'

#---------------------------------------
# SCRIPT
#---------------------------------------

test.true(delete_dir(PATH), "could not delete dir")
test.false(path.exists(PATH) and path.isdir(PATH), "temp dir found")

test.success()
