# Holds functions for printing tokens
import ax_types as types

def escape(s):
    """In case there is a quote inside of the expression, this will put a backslash in front of it,
    so it won't be processed as a list."""
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

def print_token(token, print_readably=True):
    """Takes the token and decided how to print it, depending on the type of the token."""
    # It will also take out the unnecessary whitespace or syntax errors
    # ex: if the user types:    user> (   * 44        8)
    # it will print out:        (* 44 8)

    # return as a string if the token is a symbol, int, or float since there is nothing to evaluate
    if types.is_symbol(token):
        return str(token)
    elif type(token) == int or type(token) == float:
        return str(token)

    # evaluate each part of the list/array/dictionary (in case one is a variable) and print a new list

    elif types.is_list(token):
        return "(" + " ".join([print_token(e, print_readably) for e in token]) + ")"
    elif types.is_vector(token):
        return "[" + " ".join([print_token(e, print_readably) for e in token]) + "]"
    elif types.is_dict(token):
        vecs = []
        for k in token.keys():
            vecs.extend((print_token(k), print_token(token[k], print_readably)))
        return "{" + " ".join(vecs) + "}"

    # return the string as it is. Unless the feature for readability is on,
    # meaning the user wants to see the quotes around it.
    elif type(token) == str:
        if print_readably:
            return '"' + escape(token) + '"'
        else:
            return token

    elif types.is_nil(token):
        return "nil"
    elif types.is_true(token):
        return "true"
    elif types.is_false(token):
        return "false"

    else:
        return token.__str__() # otherwise, just print a string of the token
