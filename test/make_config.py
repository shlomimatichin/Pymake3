#---------------------------------------
# IMPORTS
#---------------------------------------

from test   import *
from pymake import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target
def my_target_1(conf):
    assert_true(conf.value == '123abc', "conf.value should be '123abc'")

    conf.value = 'xyz456'

@target
@depends_on('my_target_1')
def my_target_2(conf):
    assert_true(conf.value == 'xyz456', "conf.value should be 'xyz456'")

    test_pass()

#---------------------------------------
# SCRIPT
#---------------------------------------

make('my_target_2', { 'value': '123abc' })
test_fail("my_target_2 was not invoked")
