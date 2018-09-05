#---------------------------------------
# GLOBALS
#---------------------------------------

_problems = []

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def error(s, *args):
    e = lambda: None

    e.is_error = True
    e.text = "error: " + s.format(*args)

    _problems.append(e)

def problems():
    return _problems

def warn(s, *args):
    e = lambda: None

    e.is_error = False
    e.text = "warning: " + s.format(*args)

    _problems.append(e)
