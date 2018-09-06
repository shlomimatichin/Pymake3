#---------------------------------------
# DUNDERS
#---------------------------------------

__author__  = "Philip Arvidsson <contact@philiparvidsson.com>"
__license__ = "MIT (see LICENSE)"
__version__ = "0.4.7"

#---------------------------------------
# IMPORTS
#---------------------------------------

from pymake3 import template

from pymake3.cli.main import pymake3

from pymake3.core import makeconf

from pymake3.core.decorators import (after_target, before_target, default_conf,
                                     default_target, depends_on, target)

from pymake3.core.maker import make

from pymake3.makeutils.fs import (copy, create_dir, delete_dir, delete_file,
                                  find_files, watch_files)

from pymake3.makeutils.proc import run_program, run
