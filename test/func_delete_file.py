#---------------------------------------
# IMPORTS
#---------------------------------------

from os import path

from test   import *
from pymake import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

FILENAME = 'tempfile.xyz'

#---------------------------------------
# SCRIPT
#---------------------------------------

try:
    with open(FILENAME, 'w') as f:
        f.write('foo')
except:
    test_fail("could not write to file")

assert_true(delete_file(FILENAME), "could not delete file")
assert_false(path.exists(FILENAME) and path.isfile(FILENAME), "temp file found")

test_pass()
