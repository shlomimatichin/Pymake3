#---------------------------------------
# IMPORTS
#---------------------------------------

from os import path

from test   import *
from pymake import *

#---------------------------------------
# SCRIPT
#---------------------------------------

remove_dir('temp')
assert_false(path.exists('temp') and path.isdir('temp'), "temp dir found")
test_pass()
