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
    test.success()

#---------------------------------------
# SCRIPT
#---------------------------------------

make('my_target', {})

test.fail("'my_target' was not made")
