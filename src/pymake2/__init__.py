#---------------------------------------
# DUNDERS
#---------------------------------------

__author__  = "Philip Arvidsson <contact@philiparvidsson.com>"
__license__ = "MIT (see LICENSE)"
__version__ = "0.4.7"

#---------------------------------------
# IMPORTS
#---------------------------------------

from pymake2 import template

from pymake2.cli.main import pymake2

from pymake2.core import makeconf

from pymake2.core.decorators import (after_target, before_target, default_conf,
                                     default_target, depends_on, target)

from pymake2.core.maker import make

from pymake2.makeutils.fs import (copy, create_dir, delete_dir, delete_file,
                                  find_files, watch_files)

from pymake2.makeutils.proc import run_program
