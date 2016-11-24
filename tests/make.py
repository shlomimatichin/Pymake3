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
    test.success()

#---------------------------------------
# SCRIPT
#---------------------------------------

pymake2({}, ['my_target'])

test.fail("'my_target' was not made")
