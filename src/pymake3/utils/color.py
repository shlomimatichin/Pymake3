"""
Simple utility for coloring text.
"""

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def blue(s):
    """
    Decorates the specified string with character codes for blue text.

    :param s: Text to decorate with color codes.

    :return: String containing original text wrapped with color character codes.
    """
    return '\033[94m{}\033[0m'.format(s)

def green(s):
    """
    Decorates the specified string with character codes for green text.

    :param s: Text to decorate with color codes.

    :return: String containing original text wrapped with color character codes.
    """
    return '\033[92m{}\033[0m'.format(s)

def red(s):
    """
    Decorates the specified string with character codes for red text.

    :param s: Text to decorate with color codes.

    :return: String containing original text wrapped with color character codes.
    """
    return '\033[91m{}\033[0m'.format(s)

def yellow(s):
    """
    Decorates the specified string with character codes for yellow text.

    :param s: Text to decorate with color codes.

    :return: String containing original text wrapped with color character codes.
    """
    return '\033[93m{}\033[0m'.format(s)
