#!/usr/bin/python3

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake3 import *

#---------------------------------------
# SCRIPT
#---------------------------------------

test.should_fail()

pymake3({}, [ 'my_target' ])

test.success()
