# Holds functions for printing tokens
import reader, ax_types

def print_token(token):
    "decides the type of token and prints the corresponding statement"
    if ax_types._is_symbol == True:
        print(reader.read_str)
    if type(token) == 'num':
        print(reader.read_atom)
    if type(token) == 'list':
        print(reader.read_list)
