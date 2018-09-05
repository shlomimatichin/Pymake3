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

PATH = 'tempdir'

#---------------------------------------
# SCRIPT
#---------------------------------------

create_dir(PATH)

test.true(path.exists(PATH) and path.isdir(PATH), "temp dir not found")

test.success()
