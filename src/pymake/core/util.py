#---------------------------------------
# FUNCTIONS
#---------------------------------------

def conf_merge(*args):
    r = {}

    for conf in args:
        if not conf:
            continue

        for key, value in conf.iteritems():
            r[key] = value

    return r

def conf_obj(conf):
    x = lambda: None

    for key, value in conf.iteritems():
        setattr(x, key, value)

    return x
