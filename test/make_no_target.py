#---------------------------------------
# IMPORTS
#---------------------------------------

from test   import *
from pymake import *

#---------------------------------------
# SCRIPT
#---------------------------------------

test_should_fail()

make('missing_target', {})