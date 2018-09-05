#!/usr/bin/python3

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake3 import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target
def my_target_1(conf):
    test.equal(conf.value, '123abc', "conf.value is incorrect")

    conf.value = 'xyz456'

@target
@depends_on('my_target_1')
def my_target_2(conf):
    test.equal(conf.value, '123abc', "conf.value should be immutable")

#---------------------------------------
# SCRIPT
#---------------------------------------

pymake3({ 'value': '123abc' }, [ 'my_target_2' ])

test.success()
