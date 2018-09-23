# Holds functions for printing tokens
import reader

def print_token(token):
    "decides the type of token and prints the corresponding statement"
    if _is_symbol == True:
        print(read_str)
    if type(token) == num:
        print(read_atom)
    if type(token) == list:
        print read_list

while True:
    input = raw_input("user> ")
    print(print_token(input))
