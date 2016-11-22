#---------------------------------------
# IMPORTS
#---------------------------------------

from os import path

from test   import *
from pymake import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

# Directory is created by the func_create_dir test.
DIRNAME = 'tempdir'

#---------------------------------------
# SCRIPT
#---------------------------------------

assert_true(delete_dir(DIRNAME), "could not delete dir")
assert_false(path.exists(DIRNAME) and path.isdir(DIRNAME), "temp dir found")

test_pass()
