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
def my_target(conf):
    test.equal(conf.abc, '123', "conf.abc should equal 123")
    test.success()

#---------------------------------------
# SCRIPT
#---------------------------------------

pymake2({}, [ "--conf={ 'abc' : '123' }" ])
