#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake import *

#---------------------------------------
# SCRIPT
#---------------------------------------

test.should_fail()

pymake({}, [ '--no-color', 'my_target' ])
