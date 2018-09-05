"""
Template make script for watching files for changes. Provides the 'watch' target
that continuously watches a list of files for changes. When one of the watched
files has been changed, a target spceified in the configuration will be made.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

from pymake3 import *

#---------------------------------------
# GLOBALS
#---------------------------------------

# Default configuration.
conf = makeconf.from_dict({ 'fswatcher': {
                                'extensions' : [ '*.*' ],
                                'interval'   : 0.5,
                                'path'       : 'src',
                                'target'     : 'compile'
                            } })

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def on_files_changed(conf, filenames):
    """
    This function is called after watched files have been changed. It makes the
    target specified in the fswatcher configuration.

    :param conf:      Make configuration.
    :param filenames: Names of the files that have changed.
    """
    if not filenames:
        return True

    make(conf.fswatcher.target, conf)
    return True

@target(conf=conf)
def watch(conf):
    """
    Watches files in a directory for changes, making a specified target when a
    change has been detected in any of the files.
    """
    filenames = []

    for ext in conf.fswatcher.extensions:
        filenames += find_files(conf.fswatcher.path, ext)

    watch_files(filenames, on_files_changed, conf, conf.fswatcher.interval)
