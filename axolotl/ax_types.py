# Tests what type the token is (list, vector, etc.) and how to parse them

# Symbols
class Ax_Symbol(str):
    def __str__(self):
        """Puts a quote infront of the symbol so it won't be processed."""
        return "'" + self

def is_symbol(input):
    """Tests to see if the token is a symbol"""
    return isinstance(input, Ax_Symbol)

def new_symbol(name):
    """Creates a new symbol."""
    return Ax_Symbol(name)

# list
class Ax_List(list):
    def __str__(self):
        """Turns each list value into a new list of strings."""
        slst = [str(e) for e in self]
        return "(" + " ".join(slst) + ")"

def is_list(input):
    """Tests to see if the token is a list. Returns true or false."""
    return type(input) == Ax_List

def new_list(*values):
    """Creates a new list of Ax_Lists (each value is a string)."""
    return Ax_List(values)

# vectors
class Ax_Vector(list):
    def __str__(self):
        """Will turn each array value into a string in a new array."""
        arr = [str(e) for e in self]
        return "[" + " ".join(arr) + "]"

def is_vector(input):
    """Tests to see if the token is a vector. Returns true or false."""
    return type(input) == Ax_Vector # returns True or False

def new_vec(func, array):
    """Creates a new list of Ax_Vec's (meaning each value is a string inside of it)."""
    new_vec = []
    for i in vec:
        new_vec.append(func(vec))
        i += 1
    return new_vec

# Dictionary
class Ax_Dict(list):
    def __str__(self):
        """Will turn each dictionary value into a string in a new dictionary."""
        dic = [str(e) for e in self]
        return "{" + " ".join(dic) + "}"

def is_dict(input):
    """Tests to see if the token is a dictionary. Returns true or false."""
    return type(input) == Ax_Dict

def new_dict(func, dic):
    """Creates a new dictionary and will put each value through whatever function is given."""
    new_dic = []
    for i in dic:
        new_vec.append(func(dic))
        i += 1
    return new_dic

# Keywords (:)
class Ax_Key(str):
    def __str__(self):
        """Will just return it's self, instead of turning into a string."""
        return self

def is_keyword(input):
    """Tests to see if the token is a keyword (a Key in a dictonary that points to a value)"""
    return isinstance(input, Ax_Key)

def new_keyword(name):
    "Creates a new keyword."
    return Ax_Key(name)

# Functions
def Ax_func(Eval, Env, modules, ast, defined_env, params):
    """The functions will be given as parameters so you can use any Eval function,
    environment, or modules the user wants."""

    def fn(*args): # adding a * means the parameters have no length restriction
        return Eval(ast, Env(defined_env, params, Ax_List(args)))
        # evaluates values with given evaluation functions

    return fn

def is_func(input):
    """Tests to see if the token is a function by checking if there is something callable in the parameters."""
    return callable(input)

# Scalars
# Tests to see if the expression is really none, false, true, or a string
# Will return the value if this is true.
def is_none(exp):
    return exp is None
def is_true(exp):
    return exp is True
def is_false(exp):
    return exp is False
def is_string(exp):
    if type(exp) == str:
        return True
    else:
        return False
