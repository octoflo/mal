#4: adding new functions like do, if, and lambda
import reader, printer
import ax_types as types
import env, core

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
        # (def! dec (fn* [n] (- n 1)))
        a0 = ast[0]

        if "def!" == a0:
            a1, a2 = ast[1], ast[2]
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
            a1, a2 = ast[1], ast[2]
            new_env = env.Env(local_env) # points to local_env (outer)
            for i in range(0, len(a1), 2): #goes through by 2's to get variables
                new_env.set(a1[i], EVAL(a1[i+1], new_env)) #goes through to get variable values
            return EVAL(a2, new_env)

        elif "do" == a0:
            return eval_ast(ast[len(ast)], local_env)

        elif "if" == a0:
            a1, a2 = ast[1], ast[2]
            cond = EVAL(a1, local_env)
            if cond is False or cond is None:
                if len(ast) > 3:
                    return EVAL(ast[3], local_env)
                else:
                    return None
            else:
                return EVAL(a2, local_env)

        elif "fn*" == a0:
            # ( (fn* [a b] (+ a b)) 2 3)
            # (+ a b) -> (fn* [a b] (+ a b))
            a1, a2 = ast[1], ast[2]
            return types.Ax_func(EVAL, env.Env, a2, local_env, a1)

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

# REPL Loop
if __name__ == "__main__": # if being run as a program
    repl_env = env.Env()

    for func, param in core.namespace.items():
        repl_env.set(types.new_symbol(func), param)

    while True:
        input = raw_input("user> ")
        if input == "EOF": # End of File
            break
        else:
            print REP(input, repl_env)
