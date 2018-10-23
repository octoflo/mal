import printer
import ax_types as types

def print_str(args, print_readably):
    # return map(printer.print_token, args) OR
    return [printer.print_token(e, print_readably) for e in args] # print_token returns in string form

def prn(*args):
    print(" ".join(print_str(args, True)))
    return None

def pr_str(*args):
    return " ".join(print_str(args, True))

def str(*args):
    return "".join(print_str(args, False))

def println(*args):
    print(" ".join(print_str(args, False)))
    return None

def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False

def count(lst):
    if types.is_nil(lst):
        return 0
    else:
        return len(lst)

def equal(a, b):
    """
    if a == b:
        return True
    else:
        return False
    """
    if type(b) == int and type(a) != int:
        return False
    if types.is_string(a) and types.is_string(b):
        return a == b
    elif types.is_list(a) or types.is_vector(a):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not equal(a[i], b[i]):
                return False
        return True
    else:
        return a == b

namespace = {
    'list': types.new_list,
    'list?': types.is_list,
    'empty?': is_empty,
    'count': count,
    'true?': types.is_true,
    'false?': types.is_false,
    'nil?': types.is_nil,

    'prn': prn,
    'pr-str': pr_str,
    'str': str,
    'println': println,

    '=': equal,
    '+': lambda a,b: a+b,
    '-': lambda a,b: a-b,
    '*': lambda a,b: a*b,
    '/': lambda a,b: a/b,

    '<': lambda a,b: a<b,
    '>': lambda a,b: a>b,
    '<=': lambda a,b: a<=b,
    '>=': lambda a,b: a>=b,

}
