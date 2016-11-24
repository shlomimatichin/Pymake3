#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake2 import *

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

pymake2({}, [ '--no-color' ])

test.success()
