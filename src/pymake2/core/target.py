#---------------------------------------
# IMPORTS
#---------------------------------------

from pymake2.core.conf import conf_merge, make_conf

#---------------------------------------
# CLASSES
#---------------------------------------

class Target(object):
    #---------------------------------------
    # CONSTRUCTOR
    #---------------------------------------

    def __init__(self, name, func=None):
        self.checked    = True
        self.def_conf   = {}
        self.depends    = []
        self.desc       = None
        self.func       = func
        self.name       = name
        self.post_funcs = []
        self.pre_funcs  = []

    #---------------------------------------
    # METHODS
    #---------------------------------------

    def make(self, conf):
        conf = make_conf(conf)
        conf = conf_merge(self.def_conf, conf)

        for f in self.pre_funcs:
            f(conf)

        self.func(conf)

        for f in self.post_funcs:
            f(conf)
