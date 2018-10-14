#2: interpreter for a simple number calculator by adding to the evaluator
import reader, printer
import ax_types as types

# read
def READ(input):
    return reader.get_tokens(input)

# eval
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

repl_env = {'+': sum,
            '-': sub,
            '*': mult,
            '/': div}

def eval_ast(value, repl_env): #repl_env is a parameter because you can't use + on it's own, you need to define what to use
    "subsitutes the symbol (first param) given to the function in repl_env"
    if types.is_symbol(value): # if statements returning exceptions use "try"
        try:
            return repl_env[value]
        except:
            raise Exception("'" + value + "' not found")
    elif types.is_list(value) or types.is_vec(value):
        return [EVAL(s) for s in value] #comprehension
    else:
        return value

def EVAL(ast):
    print(ast)
    print(type(ast))
    if types.is_vec(ast):
        print("I found a vec")
        return eval_ast(ast, repl_env)
    elif types.is_list(ast) and len(ast) == 0:
        return ast
    elif types.is_list(ast): # if it is an Ax_List then treat it like an instance
        lst = eval_ast(ast, repl_env)
        func = lst[0]
        return func(*lst[1:])
    else:
        return eval_ast(ast, repl_env) # could be a list inside of a list

# print
def PRINT(value):
    return printer.print_token(value)

# REPL
def REP(input):
    try:
        return PRINT(EVAL(READ(input)))
    except Exception as e:
        return str(e)

# REPL Loop
while True:
    input = raw_input("user> ")
    if input == "EOF": # End of File
        break
    else:
        print REP(input)
