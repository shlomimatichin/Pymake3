#!/usr/bin/python3

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake3 import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@default_target
def my_target(conf):
    test.success()

#---------------------------------------
# SCRIPT
#---------------------------------------

pymake3({}, [])

test.fail("'my_target' was not made")
