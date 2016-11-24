#---------------------------------------
# CLASSES
#---------------------------------------

class Target(object):
    #---------------------------------------
    # CONSTRUCTOR
    #---------------------------------------

    def __init__(self, name, func=None):
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
        conf = self.merge_confs(self.def_conf, conf)
        conf = self.dict_to_obj(conf)

        for f in self.pre_funcs:
            f(conf)

        self.func(conf)

        for f in self.post_funcs:
            f(conf)

    def dict_to_obj(self, conf):
        x = lambda: None

        for key, value in conf.iteritems():
            setattr(x, key, value)

        return x

    def merge_confs(self, *args):
        r = {}

        for conf in args:
            if not conf:
                continue

            for key, value in conf.iteritems():
                r[key] = value

        return r
