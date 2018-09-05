#!/usr/bin/python3

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake3 import *

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

pymake3({}, [ "--conf={ 'abc' : '123' }" ])
