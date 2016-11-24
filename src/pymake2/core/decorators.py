#---------------------------------------
# IMPORTS
#---------------------------------------

from pymake2            import report
from pymake2.core.maker import Maker

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def after_target(name):
    def decorator(func):
        target = Maker.inst().get_target(name)

        target.post_funcs.append(func)

        return func

    return decorator

def before_target(name):
    def decorator(func):
        target = Maker.inst().get_target(name)

        target.pre_funcs.append(func)

        return func

    return decorator

def default_conf(conf):
    def decorator(func):
        name   = func.__name__
        target = Maker.inst().get_target(name)

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
        target  = Maker.inst().get_target(name)

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
        desc    = kwargs.get('desc'   , None )
        name    = kwargs.get('name'   , None ) or func.__name__
        target  = Maker.inst().get_target(name)

        if target.func:
            report.error("target already bound: {}", name)
            return

        target.func = func

        if conf:
            target.def_conf = conf

        if default:
            if Maker.inst().def_target:
                report.warn('default target set more than once')

            Maker.inst().def_target = target

        if depends:
            # Add dependencies that are not already in the target's dependency
            # list.
            target.depends.extend(x for x in depends if x not in target.depends)

        if desc:
            target.desc = desc

        return func

    return decorator(*args) if args else decorator
