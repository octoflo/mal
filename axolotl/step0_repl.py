# Creates a simple REPL

def READ(input):
    return input

def EVAL(input):
    return input

def PRINT(input):
    return input

def rep(input, read_f, eval_f, print_f):
    return print_f(eval_f(read_f(input)))

while True:
    input = raw_input("user> ")
    if input == "EOF": # End of File
        break
    else:
        print rep(input, PRINT, EVAL, PRINT)
