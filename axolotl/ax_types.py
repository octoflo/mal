# Symbols
class Ax_Symbol(str):
    def __str__(self):
        return "'" + self

def is_symbol(input):
    "tests to see if the token is a symbol"
    return isinstance(input, Ax_Symbol)

def new_symbol(name):
    "creates a new symbol"
    return Ax_Symbol(name)

# list
class Ax_List(list):
    def __str__(self):
        slst = [str(e) for e in self]
        return "(" + " ".join(slst) + ")"

    def __add__(self, rhs): return Ax_List(list.__add__(self, rhs))
    def __getitem__(self, i):
        if type(i) == slice: return Ax_List(list.__getitem__(self, i))
        elif i >= len(self): return None
        else:                return list.__getitem__(self, i)
    def __getslice__(self, *a): return Ax_List(list.__getslice__(self, *a))

def is_list(input):
    return type(input) == Ax_List # returns True or False

def new_list(*values):
    """
    def new_list(func, list):
    new_list = []
    for i in list:
        new_list.append(func(list))
        i += 1
    return new_list"""
    return Ax_List(values)

# vectors
class Ax_Vector(list):
    def __str__(self):
        arr = [str(e) for e in self]
        return "[" + " ".join(arr) + "]"

    def __add__(self, rhs): return Ax_Vector(list.__add__(self, rhs))
    def __getitem__(self, i):
        if type(i) == slice: return Ax_Vector(list.__getitem__(self, i))
        elif i >= len(self): return None
        else:                return list.__getitem__(self, i)
    def __getslice__(self, *a): return Ax_Vector(list.__getslice__(self, *a))


def is_vector(input):
    return type(input) == Ax_Vector # returns True or False

def new_vec(func, array):
    new_vec = []
    for i in vec:
        new_vec.append(func(vec))
        i += 1
    return new_vec

# Dictionary
class Ax_Dict(list):
    def __str__(self):
        dic = [str(e) for e in self]
        return "{" + " ".join(dic) + "}"

    def __add__(self, rhs): return Ax_Dict(list.__add__(self, rhs))
    def __getitem__(self, i):
        if type(i) == slice: return Ax_Dict(list.__getitem__(self, i))
        elif i >= len(self): return None
        else:                return list.__getitem__(self, i)
    def __getslice__(self, *a): return Ax_Dict(list.__getslice__(self, *a))


def is_dict(input):
    return type(input) == Ax_Dict # returns True or False

def new_dict(func, dic):
    new_dic = []
    for i in dic:
        new_vec.append(func(dic))
        i += 1
    return new_dic

# Keywords (:)
class Ax_Key(str):
    def __str__(self):
        return self

def is_keyword(input):
    "tests to see if the token is a symbol"
    return isinstance(input, Ax_Key)

def new_keyword(name):
    "creates a new symbol"
    return Ax_Key(name)

# Scalars
def is_nil(exp):
    return exp is None
def is_true(exp):
    return exp is True
def is_false(exp):
    return exp is False

# Functions
def Ax_func(Eval, Env, # modules, so you can use any Eval function or Environment you want (instead of importing them)
            ast, defined_env, params):
    def fn(*args): # * = parameters with no length restriction
        return Eval(ast, Env(defined_env, params, Ax_List(args)))
    return fn

def is_func(input):
    # is there something callable in the parameters?
    return callable(input)
