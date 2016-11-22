#---------------------------------------
# IMPORTS
#---------------------------------------

from test   import *
from pymake import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target
def all(conf):
    test_fail()

@default_target
def my_target(conf):
    test_pass()

#---------------------------------------
# SCRIPT
#---------------------------------------

make()
