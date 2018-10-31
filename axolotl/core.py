# Defines the Axolotl specific syntax

import printer
import ax_types as types

def pr_str(args, print_readably):
    """Prints the token as a string."""
    return [printer.print_token(e, print_readably) for e in args]

def display(*args):
    """Prints the input, keeping any quotes (for a string) or other symbols with it."""
    print(" ".join(pr_str(args, True)))
    return None

def dis_str(*args):
    """Prints a string with it's quotes."""
    return " ".join(pr_str(args, True))

def string(*args):
    """Prints as tring without it's quotes."""
    return "".join(pr_str(args, False))

def display_nl(*args):
    """Prints value and goes to the next line."""
    print(" ".join(pr_str(args, False)))
    return None

def is_empty(lst):
    """Check if the given list is empty (has a length of 0)."""
    if len(lst) == 0:
        return True
    else:
        return False

def count(lst):
    """Returns how many values are in the list."""
    if types.is_nil(lst):
        return 0
    else:
        return len(lst)

def equal(a, b):
    """Checks if the two given values are equal to eachother.
    There are extra checks to make sure the types are the same as well, because
    once the values are processed "hello world" and hello world are equal to eachother."""
    ta, tb = type(a), type(b)
    if types.is_string(a) and types.is_string(b):
        return a == b

    if ta == int and tb != int:
        return False

    elif types.is_list(a) or types.is_vector(a):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not equal(a[i], b[i]):
                return False
        return True
    else:
        return a == b

def remaining(int):
    return int%2

namespace = {
    'list': types.new_list,
    'list?': types.is_list,
    'empty?': is_empty,
    'length': count,
    'true?': types.is_true,
    'false?': types.is_false,
    'none?': types.is_none,

    'display': display,
    'dis_string': dis_str,
    'string': string,
    'display_nl': display_nl,

    '=': equal,
    'sum': lambda a,b: a+b,
    'sub': lambda a,b: a-b,
    'mult': lambda a,b: a*b,
    'div': lambda a,b: a/b,
    'remaining': remaining,

    '<': lambda a,b: a<b,
    '>': lambda a,b: a>b,
    '<=': lambda a,b: a<=b,
    '>=': lambda a,b: a>=b,
}
