#---------------------------------------
# IMPORTS
#---------------------------------------

from os import path

from test   import *
from pymake import *

#---------------------------------------
# SCRIPT
#---------------------------------------

create_dir('temp')
assert_true(path.exists('temp') and path.isdir('temp'), "temp dir not found")
test_pass()
