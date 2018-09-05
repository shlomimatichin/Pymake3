#!/usr/bin/python3

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake3 import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target(name='my_target')
def my_target1(conf):
    pass

@target(name='my_target', bind='override')
def my_target2(conf):
    pass


#---------------------------------------
# SCRIPT
#---------------------------------------

pymake3({}, [ 'my_target' ])

test.success()
