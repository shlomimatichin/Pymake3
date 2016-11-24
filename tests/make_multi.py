#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake2 import *

#---------------------------------------
# GLOBALS
#---------------------------------------

var = 0

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target
def my_target(conf):
    global var
    var += 1

#---------------------------------------
# SCRIPT
#---------------------------------------

pymake2({}, [ 'my_target' ])
pymake2({}, [ 'my_target' ])
pymake2({}, [ 'my_target' ])

test.equal(var, 3, "my_target was not made three times")
test.success()
