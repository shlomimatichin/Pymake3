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
@depends_on('my_target_3')
def my_target_1(conf):
    pass

@target
@depends_on('my_target_1')
def my_target_2(conf):
    pass

@target
@depends_on('my_target_2')
def my_target_3(conf):
    pass

#---------------------------------------
# SCRIPT
#---------------------------------------

test.should_fail()

pymake2({}, [ 'my_target_3' ])

test.success()
