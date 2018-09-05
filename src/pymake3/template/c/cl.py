#!/usr/bin/python3
"""
Template make script for Microsoft's C compiler cl.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

import os

from pymake3 import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

# Path to the csc compiler to use.
CL = r'C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\amd64\cl.exe'

#---------------------------------------
# GLOBALS
#---------------------------------------

# Default configuration settings.
conf = makeconf.from_dict({
    'name'  : 'main.exe',
    'cflags': [ '/DNDEBUG', '/DUNICODE', '/O2', '/Wall' ],
    'lflags': [ '/MACHINE:AMD64' ],

    'includepaths': [ r'C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include',
                      r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.10586.0\shared',
                      r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.10586.0\ucrt',
                      r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.10586.0\um' ],

    'libpaths': [ r'C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\amd64',
                  r'C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10586.0\ucrt\x64',
                  r'C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10586.0\um\x64' ],

    'libs': [ 'kernel32.lib', 'user32.lib' ],

    'bindir': 'bin',
    'objdir': 'obj',
    'srcdir': 'src'
})

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target(conf=conf)
def clean(conf):
    """
    Cleans the build by deleting the bin and obj directories.
    """
    delete_dir(conf.bindir)
    delete_dir(conf.objdir)

@target(conf=conf)
def compile(conf):
    """
    Compiles the executable program from its sources in the source directory.
    """
    exe_file = os.path.join(conf.bindir, conf.name)

    if os.path.isfile(exe_file):
        mtime = os.path.getmtime(exe_file)
        skip  = True

        for s in find_files(conf.srcdir, [ '*.c', '*.h' ]):
            if os.path.getmtime(s) > mtime:
                skip = False
                break

        if skip:
            # No source files have changed since the last compile, so we don't
            # need to recompile.
            return

    create_dir(conf.bindir)
    create_dir(conf.objdir)

    options = (
        [ '/nologo' ] +
        conf.cflags +
        [ '/Fe' + os.path.join(conf.bindir, conf.name) ] +
        [ '/Fo' + conf.objdir + '\\' ] +
        [ '/I' + s for s in conf.includepaths] +
        find_files(conf.srcdir, '*.c') +
        conf.libs +
        [ '/link' ] +
        conf.lflags +
        [ '/LIBPATH:' + s for s in conf.libpaths ]
    )

    run_program(CL, options)

@target(conf=conf)
def run(conf):
    """
    Runs the target executable.  This target has no dependencies, so the program
    needs to be built first.
    """
    os.chdir(conf.bindir)
    run_program(conf.name)

#---------------------------------------
# SCRIPT
#---------------------------------------

if __name__ == '__main__':
    pymake3()
