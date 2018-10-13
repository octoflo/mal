# Symbols
class Symbol(str): pass # starting as a string and changing it

def _symbol(name):
    "creates a new symbol"
    return Symbol(name)

def _is_symbol(input):
    "tests to see if the token is a symbol"
    return isinstance(input, Symbol)

# list
class Ax_List(list):
    def __str__(self):
        slst = [str(e) for e in self]
        return "(" + " ".join(slst) + ")"

def _is_list(input):
    return type(input) == Ax_List # returns True or False

def new_list(func, list):
    new_list = []
    for i in list:
        new_list.append(func(list))
        i += 1
    return new_list

# Ast: Abstract Syntax Tree
def ast():
    "Abstract Syntax Tree"
