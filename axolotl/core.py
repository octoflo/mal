# Defines the Axolotl specific syntax

import printer
import ax_types as types

def pr_str(args, print_readably):
    """Prints the token as a string."""
    return [printer.print_token(e, print_readably) for e in args]

def print(*args):
    """Prints the inputs, keeping any quotes (for a string) or other symbols."""
    # Ex: with the value "hello world" it will print "hello world" rather than hello world without the quotes
    print(" ".join(pr_str(args, True)))
    return None

def print_str(*args):
    """Prints a string with it's quotes."""
    return " ".join(pr_str(args, True))

def str(*args):
    """Prints as tring without it's quotes."""
    return "".join(pr_str(args, False))

def println(*args):
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
    if not (ta == tb)

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

# In the following dictionary the keys are the Axolotl Syntax the user will type,
# and the value is what you should do with the values when the token equals that given function.
namespace = {
    'list': types.new_list,
    'list?': types.is_list,
    'empty?': is_empty,
    'count': count,
    'true?': types.is_true,
    'false?': types.is_false,
    'none?': types.is_none,

    'display': print,
    'dis_string': print_str,
    'string': str,
    'display_nl': println,

    '==': equal,
    '+': lambda a,b: a+b,
    '-': lambda a,b: a-b,
    '*': lambda a,b: a*b,
    '/': lambda a,b: a/b,

    '<': lambda a,b: a<b,
    '>': lambda a,b: a>b,
    '<=': lambda a,b: a<=b,
    '>=': lambda a,b: a>=b,
}
