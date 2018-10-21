import printer
import ax_types as types

def prnt(*args):
    print(printer.print_token(a))
    return nil

def prnt_str(*args):
    vals = printer.print_token(*args)
    return " ".join(vals)

def str(*args):
    vals = printer.print_token(*args)
    return "".join(vals)

def println(*args):
    vals = printer.print_token(*args)
    print("".join(vals))
    return nil

def is_empty(*args):
    if len(*args) == 0:
        return True
    else:
        return False

def count(*args):
    if len(*args) == 0:
        return None
    else:
        return len(*args)

def equal(a, b):
    if a == b:
        return True
    else:
        return False

namespace = {
    'list': types.new_list,
    'list?': types.is_list,
    'empty?': is_empty,
    'count': count,
    'true?': types.is_true,
    'false?': types.is_false,
    'nil?': types.is_nil,

    'prn': prnt,
    'pr-str': prnt_str,
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
