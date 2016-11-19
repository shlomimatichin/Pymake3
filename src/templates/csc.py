import os, sys
sys.path.insert(0, os.path.join('build/pymake'))
from pymake import *

NAME = 'Program.exe'

FLAGS = ['/nologo',
         #'/debug',
         #'/define:DEBUG',
         '/o',
         '/platform:x64',
         '/target:exe']

LIBS = ['PresentationCore.dll',
        'System.IO.dll',
        'System.Runtime.dll',
        'WindowsBase.dll']

LIBDIRS = [r'C:\Windows\Microsoft.NET\Framework64\v4.0.30319',
           r'C:\Windows\Microsoft.NET\Framework64\v4.0.30319\WPF']

BINDIR = 'bin'
SRCDIR = 'src'

CSC = r'C:\Program Files (x86)\MSBuild\14.0\Bin\csc.exe'

@target
@depends_on('compile')
def all():
    pass

@target
def clean():
    remove_dir(BINDIR)

@target
def compile():
    if not os.path.exists(BINDIR):
        os.mkdir(BINDIR)

    libdirs = ['/lib:' + ','.join(LIBDIRS)]
    libs    = ['/r:' + lib for lib in LIBS]
    out     = ['/out:' + os.path.join(BINDIR, NAME)]
    sources = ['/recurse:' + os.path.join(SRCDIR, '*.cs')]

    run_program(CSC, FLAGS + libdirs + libs + out + sources)

@target
def run():
    os.chdir(BINDIR)
    subprocess.call([TARGET])

pymake()
