#0: Creates a REPL
def READ(input):
    return reader.read_str(input)

def EVAL(input):
    return input

def PRINT(input):
    return printer.pr_str(input)

def rep(input, read_f, eval_f, print_f):
    return print_f(eval_f(read_f(input)))

while True:
    input = raw_input("user> ")
    if input == "EOF": # End of File
        break
    else:
        print rep(input, READ, EVAL, PRINT)

#1: Lexing and Parsing
