"""
Provides functionality for managing make configurations.
"""

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def from_dict(d):
    """
    Creates a make configuration object from an object by applying all
    attributes to it.

    :param d: Dictionary (dict) to create a make configuration object from.

    :return: Make configuration object containing the dictionary keys and values
             as attributes.
    """
    o = lambda: None

    for k, v in d.items():
        if isinstance(v, dict):
            v = from_dict(v)

        setattr(o, k, v)

    return o

def merge(*args):
    """
    Merges several make configuration objects into one in the order they are
    specified.  If several configurations contain attributes with the same
    names, the latter value will be kept (with respect to the order in which
    they were provided to this function).

    :param args: Configurations to merge.

    :return: Configuration object containing attributes from all specified
             make configurations.
    """
    d = {}

    for conf in args:
        for key, value in conf.__dict__.items():
            d[key] = value

    return from_dict(d)
