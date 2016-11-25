#---------------------------------------
# FUNCTIONS
#---------------------------------------

def make_conf(d):
    if not isinstance(d, dict):
        d = d.__dict__

    x = lambda: None

    for k, v in d.iteritems():
        if isinstance(v, dict):
            v = make_conf(v)

        setattr(x, k, v)

    return x

def conf_merge(*args):
    r = {}

    for conf in args:
        if not conf:
            continue

        conf = conf.__dict__

        for key, value in conf.iteritems():
            r[key] = value

    return make_conf(r)
