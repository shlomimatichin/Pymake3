#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import sys

sys.path.insert(0, os.path.join('build/pymake'))
from pymake import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

# Name of the program.
NAME = 'Program.exe'

# Flags specifying how to compile the program.
FLAGS = [
#    '/debug',
#    '/define:DEBUG',
    '/nologo',
    '/o',
    '/platform:x64',
    '/target:exe'
]

# Libraries needed to compile the program.
LIBS = [
    'PresentationCore.dll',
    'System.IO.dll',
    'System.Runtime.dll',
    'WindowsBase.dll',
]

# Library directories to search for libraries in.
LIBDIRS = [
    'C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\',
    'C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\WPF',
]

# Where to put the compiled binary files.
BINDIR = 'bin'

# Source code directory.
SRCDIR = 'src'

# Path to the C# compiler executable.
CSC = 'C:\\Program Files (x86)\\MSBuild\\14.0\\Bin\\csc.exe'

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target('compile')
def all():
    pass

@target()
def clean():
    if os.path.isdir(BINDIR):
        remove_dir(BINDIR)

@target()
def compile():
    if not os.path.exists(BINDIR):
        os.mkdir(BINDIR)

    flags   = FLAGS
    libdirs = ['/lib:' + ','.join(LIBDIRS)]
    libs    = ['/r:' + s for s in LIBS]
    out     = ['/out:' + os.path.join(BINDIR, NAME)]
    sources = ['/recurse:' + os.path.join(SRCDIR, '*.cs')]

    run_cmd(CSC, flags + libdirs + libs + out + sources)

@target()
def run():
    os.chdir(BINDIR)
    subprocess.call([TARGET])

#---------------------------------------
# SCRIPT
#---------------------------------------

make()
