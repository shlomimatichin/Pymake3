#---------------------------------------
# IMPORTS
#---------------------------------------

from os import path

import test

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
    test.fail("could not write to file")

test.true(delete_file(FILENAME), "could not delete file")
test.false(path.exists(FILENAME) and path.isfile(FILENAME), "temp file found")

test.success()
