#---------------------------------------
# IMPORTS
#---------------------------------------

from test   import *
from pymake import *

#---------------------------------------
# GLOBALS
#---------------------------------------

global_var = 0

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target
def my_target(conf):
    global global_var
    global_var += 1

#---------------------------------------
# SCRIPT
#---------------------------------------

make('my_target', {})
make('my_target', {})
make('my_target', {})

assert_equal(global_var, 3, "my_target was not invoked three times")
