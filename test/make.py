#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target
def my_target(conf):
    test.success()

#---------------------------------------
# SCRIPT
#---------------------------------------

pymake({}, ['my_target'])

test.fail("'my_target' was not made")
