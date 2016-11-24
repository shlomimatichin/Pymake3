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
@target
def my_target(conf):
    pass

#---------------------------------------
# SCRIPT
#---------------------------------------

test.should_fail()

pymake2({}, [])

test.success()
