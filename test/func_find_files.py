#---------------------------------------
# IMPORTS
#---------------------------------------

from os.path import join

from test   import *
from pymake import *

#---------------------------------------
# SCRIPT
#---------------------------------------

files = find_files('temp', '*.txt')

assert_true(len(files) == 3, "incorrect number of files found")

assert_true(join('temp',         'file1.txt') in files, "file1.txt not found")
assert_true(join('temp',         'file2.txt') in files, "file2.txt not found")
assert_true(join('temp', 'dir1', 'file3.txt') in files, "file4.txt not found")

assert_false(join('temp',         'foo.zzz') in files, "foo.zzz found")
assert_false(join('temp', 'dir1', 'bar.zzz') in files, "bar.zzz found")
