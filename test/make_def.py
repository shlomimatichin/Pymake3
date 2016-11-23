#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@default_target
def my_target(conf):
    test.success()

#---------------------------------------
# SCRIPT
#---------------------------------------

pymake({}, [])

test.fail("'my_target' was not made")
