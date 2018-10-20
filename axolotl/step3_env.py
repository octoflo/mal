#3: adding the ability to make functions and variables
import reader, printer
import ax_types as types
import env

# read
def READ(input):
    return reader.get_tokens(input)

def eval_ast(ast, local_env): #repl_env is a parameter because you can't use + on it's own, you need to define what to use
    "subsitutes the symbol (first param) given to the function in repl_env"
    if types.is_symbol(ast):
        return local_env.get(ast) # get is in the env class (instance of repl_env)
    elif types.is_list(ast): # if statements returning exceptions use "try"
        return types.Ax_List(eval_sequence(ast, local_env))
    elif types.is_vector(ast):
        return types.Ax_Vector(eval_sequence(ast, local_env))
    else:
        return ast

def eval_sequence(seq, local_env):
    """ Evaluates each element in the sequence """
    def eval_with_local(element):
        # can use the parameters from the outside parameters (helper function)
        return EVAL(element, local_env)
    return map(eval_with_local, seq)

def EVAL(ast, local_env):
    if types.is_list(ast) and len(ast) == 0:
        # empty list: ()
        return ast
    elif types.is_list(ast):
        a0, a1, a2 = ast[0], ast[1], ast[2]

        if "def!" == a0:
            # defining a variable
            # (def! x 3)
            value = EVAL(a2, local_env)
            local_env.set(a1, value) # puts it in the local env dictionary
            return value

        elif "let*" == a0:
            # It's a way to define function and variables in the same space
            # (let* ((x 1) a0: function name
            # (y 2)) a1: variables
            # (+ x y)) a2: script
            # in axolotl:
            # (let* [x 3 y 4] (+ x y))

            new_env = env.Env(local_env) # points to local_env (outer)
            for i in range(0, len(a1), 2): #goes through by 2's to get variables
                new_env.set(a1[i], EVAL(a1[i+1], new_env)) #goes through to get variable values
            return EVAL(a2, new_env)
        else:
            # If just a regular list:
            el = eval_ast(ast, local_env)
            f = el[0]
            return f(*el[1:])
    else:
        return eval_ast(ast, local_env)

# print
def PRINT(value):
    return printer.print_token(value)

# REPL
def REP(input, global_env):
    try:
        return PRINT(EVAL(READ(input), global_env))
    except Exception as e:
        return str(e)

def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

# REPL Loop
if __name__ == "__main__": # if being run as a program
    repl_env = env.Env()
    repl_env.set('+', sum)
    repl_env.set('-', sub)
    repl_env.set('*', mult)
    repl_env.set('/', div)

    while True:
        input = raw_input("user> ")
        if input == "EOF": # End of File
            break
        else:
            print REP(input, repl_env)
