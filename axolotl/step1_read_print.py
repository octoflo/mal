#1: Lexing and Parsing
import reader, printer

def READ(input):
    return reader.read_str(input)

def EVAL(input):
    return input

def PRINT(input):
    return printer.pr_str(input)

def rep(input, read_f, eval_f, print_f):
    return printer.print_token(PRINT(EVAL(READ(input)))

while True:
    input = raw_input("user> ")
    if input == "EOF": # End of File
        break
    else:
        print rep(input, READ, EVAL, PRINT)
