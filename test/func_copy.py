#---------------------------------------
# IMPORTS
#---------------------------------------

from test   import *
from pymake import *

#---------------------------------------
# SCRIPT
#---------------------------------------

assert_equal(copy('files', 'temp', '*.txt'), 3, "wrong number of files copied")
test_pass()
