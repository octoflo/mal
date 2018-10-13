#2: interpreter for a simple number calculator by adding to the evaluator
import reader, printer
import ax_types as types

# reader.tokenize(ast) #??

# read
def READ(ast):
    return reader.read_str(ast)

# eval
def eval_ast(ast, repl_env): #repl_env is a parameter because you can't use + on it's own, you need to define what to use
    print(ast)
    if types._is_symbol(ast): # if statements returning exceptions use "try"
        try:
            return repl_env[ast]
        except:
            raise Exception("'" + ast + "' not found")
    elif types._is_list(ast):
        types.new_list(EVAL, ast)
    else:
        return ast

def EVAL(ast):
    if not reader._is_list(ast):
        return eval_ast(ast, repl_env)

    if len(ast) == 0:
        return ast

    if reader.is_list(ast):
        list == eval_ast(ast, repl_env)
        func == list[0]
        return func(*list[1:]) #?? whats the *


# print
def PRINT(ast):
    return printer.pr_str(ast)

# REPL
repl_env = {} #??
def REP(ast):
    return PRINT(EVAL(READ(ast), repl_env))

repl_env = {'+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b)}

# REPL Loop
while True:
    input = raw_input("user> ")
    if input == "EOF": # End of File
        break
    else:
        print REP(input)
