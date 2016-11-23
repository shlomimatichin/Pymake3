#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

var_1 = 0
var_2 = 0
var_3 = 0
var_4 = 0
var_5 = ''

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target
def my_target_1(conf):
    global var_1
    var_1 += 1

    global var_5
    var_5 += '1'

@target
def my_target_2(conf):
    global var_2
    var_2 += 1

    global var_5
    var_5 += '2'

@target
@depends_on('my_target_2', 'my_target_1')
def my_target_3(conf):
    global var_3
    var_3 += 1

    global var_5
    var_5 += '3'

@target
@depends_on('my_target_1', 'my_target_3')
def my_target_4(conf):
    global var_4
    var_4 += 1

    global var_5
    var_5 += '4'

@target
@depends_on('my_target_1', 'my_target_4')
def my_target_5(conf):
    test.equal(var_1, 1     , "target 1 made incorrect number of times")
    test.equal(var_2, 1     , "target 2 made incorrect number of times")
    test.equal(var_3, 1     , "target 3 made incorrect number of times")
    test.equal(var_4, 1     , "target 4 made incorrect number of times")
    test.equal(var_5, '1234', "targets made in incorrect order")

#---------------------------------------
# SCRIPT
#---------------------------------------

pymake({}, [ 'my_target_5' ])

test.success()
