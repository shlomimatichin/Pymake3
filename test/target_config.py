#---------------------------------------
# IMPORTS
#---------------------------------------

from test   import *
from pymake import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target
def my_target(conf):
    assert_true(conf.value == '123abc', "conf.value should be '123abc'")
    test_pass()

#---------------------------------------
# SCRIPT
#---------------------------------------

make('my_target', { 'value': '123abc' })
test_fail("my_target was not invoked")
