#---------------------------------------
# IMPORTS
#---------------------------------------

from os import path

import test

from pymake3 import *

#---------------------------------------
# SCRIPT
#---------------------------------------

r = run_program('python', ['--version'])
test.equal(r, 0, 'run_program() returned incorrect value')

test.success()
