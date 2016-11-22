#---------------------------------------
# IMPORTS
#---------------------------------------

from test   import *
from pymake import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target
def my_target(conf):
    test_pass()

#---------------------------------------
# SCRIPT
#---------------------------------------

make('my_target', {})
test_fail("my_target was not invoked")
