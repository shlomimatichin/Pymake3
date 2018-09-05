"""
Provides the core pymake3 decorators for marking functions as targets and more.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

from pymake3            import report
from pymake3.core       import makeconf
from pymake3.core.maker import Maker

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
    if isinstance(conf, dict):
        conf = makeconf.from_dict(conf)

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
        bind    = kwargs.get('bind'   , None)
        default = kwargs.get('default', False)
        depends = kwargs.get('depends', None )
        desc    = kwargs.get('desc'   , None ) or func.__doc__
        name    = kwargs.get('name'   , None ) or func.__name__
        target  = Maker.inst().get_target(name)

        if target.func and bind != 'override':
            report.error("target already bound: '{}'", name)
            return

        target.func = func

        if conf:
            if isinstance(conf, dict):
                conf = makeconf.from_dict(conf)

            target.def_conf = conf

        if default:
            if Maker.inst().def_target:
                report.warn("default target set more than once.")

            Maker.inst().def_target = target

        if depends:
            # Add dependencies that are not already in the target's dependency
            # list.
            target.depends.extend(x for x in depends if x not in target.depends)

        if desc:
            desc = desc.replace('\n', '').replace('\r', '').strip()

            i = len(desc)
            while True:
                desc = desc.replace('  ', ' ')
                j = len(desc)
                if i == j:
                    break

                i = j

            target.desc = desc

        return func

    return decorator(*args) if args else decorator
