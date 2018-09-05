#!/usr/bin/python3
"""
Template make script for pdflatex.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import time

from pymake3 import *

#---------------------------------------
# GLOBALS
#---------------------------------------

# Default configuration.
conf = makeconf.from_dict({ 'bindir'  : 'bin',
                            'flags'   : [ '-file-line-error',
                                          '-halt-on-error' ],
                            'srcdir'  : 'src',
                            'srcfile' : 'main.tex' })

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target(conf=conf)
def clean(conf):
    """
    Cleans the build by deleting the bin directory and all its contents.
    """
    delete_dir(conf.bindir)

@target(conf=conf)
def compile(conf):
    """
    Compiles the LaTeX document from its sources in the source directory.
    """
    pdf_file = os.path.join(conf.bindir, conf.name)

    if not pdf_file.endswith('.pdf'):
        pdf_file += '.pdf'

    if os.path.isfile(pdf_file):
        mtime = os.path.getmtime(pdf_file)
        skip  = True

        for s in find_files(conf.srcdir, '*.*'):
            if os.path.getmtime(s) > mtime:
                skip = False
                break

        if skip:
            # No source files have changed since the last compile, so we don't
            # need to recompile.
            return

    create_dir(conf.bindir)

    bindir = os.path.abspath(conf.bindir)
    srcdir = os.path.abspath(conf.srcdir)

    flags      = conf.flags
    jobname    = [ '-jobname'         , conf.name                       ]
    output_dir = [ '-output-directory', os.path.relpath(bindir, srcdir) ]
    srcfile    = conf.srcfile

    cwd = os.getcwd()

    os.chdir(srcdir)
    run_program('pdflatex', flags + jobname + output_dir + [srcfile])
    os.chdir(cwd)

#---------------------------------------
# SCRIPT
#---------------------------------------

if __name__ == '__main__':
    pymake3()
