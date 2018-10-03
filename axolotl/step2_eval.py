#2: interpreter for a simple number calculator by adding to the evaluator
import reader, printer, ax_types

repl_env = {'+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b)}

# read
def READ(ast):
    return reader.read_str(ast)

# eval
def eval_ast(ast):
    if ax_types._is_symbol(ast): # if statements returning exceptions should be "try"
        try:
            return repl_env[ast]
        except:
            raise Exception("'" + ast + "' not found")
    elif ax_types._is_list(ast):
        ax_types.new_list(EVAL, ast)
    else:
        return ast

def EVAL(ast):
    if reader._is_list(ast) == 'list':
        # If it is a list:
        if ast[0] == None: # ?? Or if len(ast) == 0: return ast # If it is an empty list
            return ast
        else: # Treat the first value as the function name and the others as arguments
            eval_list = eval_ast(ast)
            func = eval_list[0]
            return func(*eval_list[1:]) #??
    else: # If it is not a list
        eval_ast(ast)

# print
def PRINT(ast):
    return printer.pr_str(ast)

# REPL
def REP(ast):
    return PRINT(EVAL(READ(ast)))

# REPL Loop
while True:
    input = raw_input("user> ")
    if input == "EOF": # End of File
        break
    else:
        print REP(input)
