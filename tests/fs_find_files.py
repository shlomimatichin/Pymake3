#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

from os.path import join

import test

from pymake2 import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

# Test files are copied into this folder by the fs_copy test.
PATH = 'files2'

#---------------------------------------
# SCRIPT
#---------------------------------------

files = find_files(PATH, '*.txt')

test.equal(len(files), 3, "incorrect number of files found")

test.true(join(PATH,         'file1.txt') in files, "file1.txt not found")
test.true(join(PATH,         'file2.txt') in files, "file2.txt not found")
test.true(join(PATH, 'dir1', 'file3.txt') in files, "file4.txt not found")

test.false(join(PATH,         'foo.zzz') in files, "foo.zzz found")
test.false(join(PATH, 'dir1', 'bar.zzz') in files, "bar.zzz found")

delete_dir(PATH)

test.success()
