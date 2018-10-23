# Holds functions for printing tokens
import ax_types as types

def escape(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

def print_token(token, print_readably=True):
    """decides the type of token and prints the corresponding statement
    user> (+ 4 5)
    (+ 4 5)
    user> (   * 44        8)
    (* 44 8) """
    if types.is_symbol(token):
        return str(token)
    elif type(token) == int or type(token) == float:
        return str(token)
    elif types.is_list(token):
        return "(" + " ".join([print_token(e, print_readably) for e in token]) + ")"
    elif types.is_vector(token):
        return "[" + " ".join([print_token(e, print_readably) for e in token]) + "]"
    elif types.is_dict(token):
        vecs = []
        for k in token.keys():
            vecs.extend((print_token(k), print_token(token[k], print_readably)))
        return "{" + " ".join(vecs) + "}"
        #return str(token)
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
        return token.__str__() #prints a string of the token
