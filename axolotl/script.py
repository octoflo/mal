# Functions for reading, evaluating and printing tokens. This is the main code to be run.

import reader, printer
import ax_types as types
import env, core

# READ TOKENS
def READ(input):
    """Tokenizes input from the reader file."""
    return reader.get_tokens(input)

def eval_ast(ast, local_env):
    """Evaluates the ast based on it's type."""
    # the environment is a parameter because you may need to substitute
    # paramters defined in the environment, like a +

    if types.is_symbol(ast):
        return local_env.get(ast)
    elif types.is_list(ast):
        return types.Ax_List(eval_sequence(ast, local_env))
    elif types.is_vector(ast):
        return types.Ax_Vector(eval_sequence(ast, local_env))
    else:
        return ast

def eval_sequence(seq, local_env):
    """ Evaluates each element in the sequence."""
    def eval_with_local(element):
        """This helper function only evaluates with the local environemnt."""
        return EVAL(element, local_env)
    return map(eval_with_local, seq)

def EVAL(ast, local_env):
    """The main evaluating function. Looks if the ast token is an Axolotl function name."""

    if types.is_list(ast) and len(ast) == 0: # if an empty list, return ()
        return ast
    elif types.is_list(ast):
        a0 = ast[0]

        # checks if the following function names are the first token:
        if "var" == a0:
            # defines a variable
            # ex. (var x 3)
            a1, a2 = ast[1], ast[2] # a1: variable name, a2: variable value
            value = EVAL(a2, local_env) # evaluates the variable value
            local_env.set(a1, value) # puts the variable name in the local env dictionary
            return value

        elif "function" == a0:
            # define a function and variables in the same space
            # ex. (function addition [x 3 , y 4] (sum x y))

            a1, a2 = ast[1], ast[2] # a1: variables, a2: script
            new_env = env.Env(local_env) # creates a copy of the local environment to add the func and variables to
            for i in range(0, len(a1), 2): # goes through the everyother value of the list to get variable values
                new_env.set(a1[i], EVAL(a1[i+1], new_env))
            return EVAL(a2, new_env)

        elif "output" == a0:
            # Executes multiple expressions but only returns the last one
            # ex. (output (var a 6) 7 (sum a 8))
            # When defining a variable if will usually return that variable. sd
            # Instead it will return the last statement (a + 8), returning 14

            results = [EVAL(e, local_env) for e in ast[1:]]
            return results[-1]

        elif "if" == a0:
            # if the parameter is true it will run the code below it.
            # ex. If we are given a true statement, then (if true 7 8)
            # since it's true it will return 7 (if it was false it would return 8)
            a1, a2 = ast[1], ast[2]
            cond = EVAL(a1, local_env)
            if cond is False or cond is None:
                if len(ast) > 3: # makes sure we have code to run, and not just the statement itself
                    return EVAL(ast[3], local_env)
                else:
                    return None
            else:
                return EVAL(a2, local_env)

        elif "func" == a0:
            # Creates an unnamed function (similar to lambda in other languages)
            # ex. ((func [a b] (sum a b)) 2 3)
            # we create a function that takes an a and b and adds them together.
            # a and b are 2 and 3, so the function should return 5
            a1, a2 = ast[1], ast[2]
            return types.Ax_func(EVAL, env.Env, a2, local_env, a1)

        else:
            # If it's just a regular list then parse through and evaluate each element
            el = eval_ast(ast, local_env)
            f = el[0]
            return f(*el[1:])
    else:
        return eval_ast(ast, local_env)

# print
def PRINT(value):
    return printer.print_token(value)

# REPL
repl_env = env.Env() # creates outer, global environment

def REP(input, global_env):
    try: # as long as there are no exception errors, make a REPL (read, eval, print) of the input
        return PRINT(EVAL(READ(input), global_env))
    except Exception as e:
        return str(e)

for func, param in core.namespace.items():
    # takes the function names set in core, and puts them inside repl_env enviornment
    repl_env.set(types.new_symbol(func), param)

# If there is not a function given return false, otherwise return true
# REP("(var not (function (a) (if a false true)))", repl_env)

# REPL Loop
if __name__ == "__main__": # if being run as the main program, run the following code

    while True:
        input = raw_input("human> ") # Creates a space for user input
        if input == "EOF": # Quit REPL by typing EOF (End of File)
            break
        else:
            print REP(input, repl_env)
