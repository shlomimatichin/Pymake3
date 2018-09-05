#!/usr/bin/python3

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake3 import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@default_conf({})
def my_target():
    pass

#---------------------------------------
# SCRIPT
#---------------------------------------

test.should_fail()

pymake3({}, [ 'my_target' ])

test.success()
