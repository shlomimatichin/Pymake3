#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake2 import *

#---------------------------------------
# SCRIPT
#---------------------------------------

test.should_fail()

pymake2({}, [ 'my_target' ])

test.success()
