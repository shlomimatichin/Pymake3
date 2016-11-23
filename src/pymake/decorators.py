#---------------------------------------
# IMPORTS
#---------------------------------------

import pymake

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def after_target(name):
    def decorator(func):
        target = pymake.inst.get_target(name)

        target.post_funcs.append(func)

        return func

    return decorator

def before_target(name):
    def decorator(func):
        target = pymake.inst.get_target(name)

        target.pre_funcs.append(func)

        return func

    return decorator

def default_conf(conf):
    def decorator(func):
        name   = func.__name__
        target = pymake.inst.get_target(name)

        target.def_conf = conf

        return func

    return decorator

def default_target(*args, **kwargs):
    kwargs['default'] = True

    return target(*args, **kwargs)

def depends_on(*args):
    def decorator(func):
        depends = args
        name    = func.__name__
        target  = pymake.inst.get_target(name)

        if depends:
            # Add dependencies that are not already in the target's dependency
            # list.
            target.depends.extend(x for x in depends if x not in target.depends)

        return func

    return decorator

def target(*args, **kwargs):
    def decorator(func):
        conf    = kwargs.get('conf'   , None )
        default = kwargs.get('default', False)
        depends = kwargs.get('depends', None )
        name    = kwargs.get('name'   , None ) or func.__name__
        target  = pymake.inst.get_target(name)

        target.func = func

        if conf:
            target.def_conf = conf

        if default:
            if pymake.inst.def_target:
                pymake.warn('default target set more than once')

            pymake.inst.def_target = target

        if depends:
            # Add dependencies that are not already in the target's dependency
            # list.
            target.depends.extend(x for x in depends if x not in target.depends)

        return func

    return decorator(*args) if args else decorator
