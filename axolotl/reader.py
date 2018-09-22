# Holds functions related to the reader

def next(string, p):
    # returns token at current position, imcrements position
    return tokens[p]
    p++

def peak():
    # returns token
    return tokens[p]

def tokenizer(string):
    # takes a string and returns an array with tokens
    [\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"|;.*|[^\s\[\]{}('"`,;)]*)
    #  1  #2#       3       #        4         #           5           #
    # 1: ignores white space
    # 2: tokenizes special characters
    # 3: tokenizes {}, (), []
    # 4: Starts and stops in between "", unless a backlash is used
    # 5: tokenizes non-special characters (true, false, null)

def read_str:

def read_form(character):
    # reads the first token in the reader object
    if character == (:
        read_list(character)
    else:
        read_atom(character)

def read_list(character):
    while True:
        read_form(character)
        if character == ):
            break
        elif character == EOF:
            print "ERROR"

def read_atom(token):
    # returns appropriate data type value based on given token
    return type(token)
