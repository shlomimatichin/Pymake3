#---------------------------------------
# IMPORTS
#---------------------------------------

import util

#---------------------------------------
# CLASSES
#---------------------------------------

class Target(object):
    def __init__(self, name, func=None):
        self.def_conf   = {}
        self.depends    = []
        self.func       = func
        self.name       = name
        self.post_funcs = []
        self.pre_funcs  = []

    def make(self, conf):
        conf = util.conf_merge(self.def_conf, conf)
        conf = util.conf_obj(conf)

        for f in self.pre_funcs:
            f(conf)

        self.func(conf)

        for f in self.post_funcs:
            f(conf)
