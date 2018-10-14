# Symbols
class Symbol(str):
    def __str__(self):
        return "'" + self

def _symbol(name):
    "creates a new symbol"
    return Symbol(name)

def is_symbol(input):
    "tests to see if the token is a symbol"
    return isinstance(input, Symbol)

# list
class Ax_List(list):
    def __str__(self):
        slst = [str(e) for e in self]
        return "(" + " ".join(slst) + ")"

def is_list(input):
    return type(input) == Ax_List # returns True or False

def new_list(func, list):
    new_list = []
    for i in list:
        new_list.append(func(list))
        i += 1
    return new_list

# vectors
class Ax_Vector(list):
    def __str__(self):
        arr = [str(e) for e in self]
        return "[" + " ".join(arr) + "]"

def is_vec(input):
    return type(input) == Ax_Vector # returns True or False

def new_vec(func, array):
    new_vec = []
    for i in vec:
        new_vec.append(func(vec))
        i += 1
    return new_vec
