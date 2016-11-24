#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake2 import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@default_target
def my_target_1(conf):
    test.fail("only the last default target should be called")

@default_target
def my_target_2(conf):
    test.success()

#---------------------------------------
# SCRIPT
#---------------------------------------

pymake2({}, [ '--no-warn' ])

test.fail("'my_target_2' was not made")
