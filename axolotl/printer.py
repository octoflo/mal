# Holds functions for printing tokens
import ax_types as types

def print_token(token):
    """decides the type of token and prints the corresponding statement
    user> (+ 4 5)
    (+ 4 5)
    user> (   * 44        8)
    (* 44 8) """

    if types.is_symbol(token):
        return str(token)
    elif type(token) == int or type(token) == float:
        return str(token)
    elif type(token) == str or types.is_list(token) or types.is_vector or types.is_dict:
        return str(token)
    else:
        print(token)
        print(type(token))
        return "What!? {0} is a {1}".format(token, type(format))
