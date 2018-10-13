#1: Lexing and Parsing
import reader, printer

def READ(input): #input means it's been parsed
    return reader.get_tokens(input)

def EVAL(ast):
    return ast

def PRINT(value):
    return printer.print_token(value)

def REP(input):
    try:
        return PRINT(EVAL(READ(input)))
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    while True:
        input = raw_input("user> ")
        if input == "EOF": # End of File
            break
        else:
            print REP(input)
