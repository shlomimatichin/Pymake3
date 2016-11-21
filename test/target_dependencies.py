#---------------------------------------
# IMPORTS
#---------------------------------------

from test   import *
from pymake import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

global_var_1 = 0
global_var_2 = 0
global_var_3 = 0
global_var_4 = 0
global_var_5 = ''

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target
def my_target_1(conf):
    global global_var_1
    global_var_1 += 1

    global global_var_5
    global_var_5 += '1'

@target
def my_target_2(conf):
    global global_var_2
    global_var_2 += 1

    global global_var_5
    global_var_5 += '2'

@target
@depends_on('my_target_2', 'my_target_1')
def my_target_3(conf):
    global global_var_3
    global_var_3 += 1

    global global_var_5
    global_var_5 += '3'

@target
@depends_on('my_target_1', 'my_target_3')
def my_target_4(conf):
    global global_var_4
    global_var_4 += 1

    global global_var_5
    global_var_5 += '4'

@target
@depends_on('my_target_1', 'my_target_4')
def my_target_5(conf):
    assert_equal(global_var_1, 1, "target 1 invoked incorrent number of times")
    assert_equal(global_var_2, 1, "target 2 invoked incorrent number of times")
    assert_equal(global_var_3, 1, "target 3 invoked incorrent number of times")
    assert_equal(global_var_4, 1, "target 4 invoked incorrent number of times")
    assert_equal(global_var_5, '1234', "targets invoked in incorrect order")
    test_pass()

#---------------------------------------
# SCRIPT
#---------------------------------------

make('my_target_5', {})
test_fail("my_target_5 was not invoked")
