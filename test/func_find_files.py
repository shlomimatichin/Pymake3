#---------------------------------------
# IMPORTS
#---------------------------------------

from os.path import join

from test   import *
from pymake import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

# Test files are copied into this folder by the func_copy test.
DIRNAME = 'files2'

#---------------------------------------
# SCRIPT
#---------------------------------------

files = find_files(DIRNAME, '*.txt')

assert_true(len(files) == 3, "incorrect number of files found")

assert_true(join(DIRNAME,         'file1.txt') in files, "file1.txt not found")
assert_true(join(DIRNAME,         'file2.txt') in files, "file2.txt not found")
assert_true(join(DIRNAME, 'dir1', 'file3.txt') in files, "file4.txt not found")

assert_false(join(DIRNAME,         'foo.zzz') in files, "foo.zzz found")
assert_false(join(DIRNAME, 'dir1', 'bar.zzz') in files, "bar.zzz found")

delete_dir(DIRNAME)

test_pass()
