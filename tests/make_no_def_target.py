#!/usr/bin/python3

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake3 import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target
def my_target(conf):
    # This target is not set to be the default target, so it should not be made.
    pass

#---------------------------------------
# SCRIPT
#---------------------------------------

test.should_fail()

pymake3({}, [])

test.success()
