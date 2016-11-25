"""
Template make script for watching files for changes.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

from pymake2 import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

# Default configuration.
DEFAULT_CONF = { 'fswatcher': {
                     'extensions' : [ '*.*' ],
                     'interval'   : 0.5,
                     'path'       : 'src',
                     'target'     : 'compile'
                 } }

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def on_files_changed(conf, filenames):
    if not filenames:
        return True

    make(conf.fswatcher.target, conf)
    return True

@target(conf=DEFAULT_CONF)
def watch(conf):
    """
    Watches files in a directory for changes, making a specified target when a
    change has been detected in any of the files.
    """

    filenames = []

    for ext in conf.fswatcher.extensions:
        filenames += find_files(conf.fswatcher.path, ext)

    watch_files(filenames, on_files_changed, conf, conf.fswatcher.interval)
