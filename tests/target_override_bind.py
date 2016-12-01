#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake2 import *

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

pymake2({}, [ 'my_target' ])

test.success()
