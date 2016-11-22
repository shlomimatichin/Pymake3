#---------------------------------------
# IMPORTS
#---------------------------------------

from os import path

from test   import *
from pymake import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

DIRNAME = 'tempdir'

#---------------------------------------
# SCRIPT
#---------------------------------------

create_dir(DIRNAME)
assert_true(path.exists(DIRNAME) and path.isdir(DIRNAME), "temp dir not found")

test_pass()
