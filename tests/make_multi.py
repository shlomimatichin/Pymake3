#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake import *

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

pymake({}, [ 'my_target' ])
pymake({}, [ 'my_target' ])
pymake({}, [ 'my_target' ])

test.equal(var, 3, "my_target was not made three times")
test.success()
