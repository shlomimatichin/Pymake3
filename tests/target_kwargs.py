#!/usr/bin/python3

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake3 import *

#---------------------------------------
# GLOBALS
#---------------------------------------

counter = 0

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target
def my_target1(foo=None, bar=None):
    test.equal(foo, "123", "foo has wrong value 1")
    test.equal(bar, "abc", "bar has wrong value 1")

    global counter
    counter += 1

@target
def my_target2(bar='789', foo="xyz"):
    test.equal(foo, "123", "foo has wrong value 2")
    test.equal(bar, "abc", "bar has wrong value 2")

    global counter
    counter += 1

#---------------------------------------
# SCRIPT
#---------------------------------------

pymake3({"foo": "123", "bar": "abc"}, ['my_target1', 'my_target2'])

test.equal(counter, 2, "both targets were not made properly")
test.success()
