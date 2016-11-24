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
def my_target1(conf):
    test.equal(conf.foo, '123', "conf.foo should equal '123'")

    conf.foo = 'abc'
    make('my_target2', conf)

@target
def my_target2(conf):
    test.equal(conf.foo, 'abc', "conf.foo should equal 'abc'")
    test.success()

#---------------------------------------
# SCRIPT
#---------------------------------------

make('my_target1', { 'foo': '123' })

test.fail("'my_target1' was not made")
