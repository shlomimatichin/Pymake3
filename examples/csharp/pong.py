#!/usr/bin/env python

# This is the make script for Pong - a C# source project - with some added
# comments for clarity.  See https://github.com/philiparvidsson/Pong for  more
# information.

import os, sys
sys.path.insert(0, os.path.join('build', 'pymake'))
from pymake import *

import csc

@default_target
@depends_on('compile', 'content', 'libs')
def all(conf):
    # The 'all' target doesn't need to do anything - it just depends on other
    # relevant targets to make.
    pass

@target
def content(conf):
    # Copy 'res' folder to 'Content' folder in the bin directory.
    copy('res', os.path.join(conf.bindir, 'Content'))

@target
def libs(conf):
    # Copy the SharpDX dll-files to the bin directory.
    copy(r'lib\SharpDX', conf.bindir, '*.dll')

# The configuration below depends on the backend used for the make process.  In
# this case, we're using csc, which uses the options set below.
pymake({ 'name'   : 'Pong.exe',

         'flags'  : ['/target:winexe',
                     #'/debug',
                     #'/define:DEBUG',
                     '/o',
                     '/platform:x64'],
         'libdirs': [r'lib\SharpDX'],

         'libs'   : ['PresentationCore.dll',
                     'System.IO.dll',
                     'System.Runtime.dll',
                     'WindowsBase.dll',

                     'SharpDX.D3DCompiler.dll',
                     'SharpDX.DXGI.dll',
                     'SharpDX.Direct3D11.dll',
                     'SharpDX.Mathematics.dll',
                     'SharpDX.XAudio2.dll',
                     'SharpDX.dll'] })
