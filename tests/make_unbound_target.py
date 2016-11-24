#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake2 import *

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

pymake2({}, [ 'my_target' ])

test.success()
