#---------------------------------------
# IMPORTS
#---------------------------------------

from os import path

from test   import *
from pymake import *

#---------------------------------------
# SCRIPT
#---------------------------------------

r = run_program('python', ['--version'])
assert_equal(r, 0, 'run_program() returned incorrect value')
test_pass()
