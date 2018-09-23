# Holds functions for reading/processing tokens
import re # for the ability to use regular expressions

class BlankError(Exception): pass # an exception class with a fancy name
class Symbol(str): pass # starting as a string and changing it

class Symbol:
    def __init__(self, name):
        self.name = name

def _symbol(name):
     return Symbol(name)
def _is_symbol(thing):
    return isinstance(thing, Symbol)

class Reader:
    def __init__(self, tokens, position=0):
        self.tokens = tokens
        self.position = position

    def peak(self):
        "returns token at current position"
        return self.tokens[self.position]

    def next(self):
        "returns token at current position, imcrements position"
        results = self.tokens[self.position]
        self.position += 1
        return results

def tokenize(string):
    "takes a string and returns an array with tokens"
    pattern = re.compile(r"""

    [\s,]*                # Matches any number of whitespaces or commas, it will be ignored and not tokenized.
    (
      ~@                  # Captures the special two-characters ~@ (tokenized).
     |
       [\[\]{}()'`~^@]    # Captures any special single character, one of []{}()'`~^@ (tokenized).
     |
       "(?:\\.|[^\\"])*"? # (Strings) Starts capturing at a double-quote and stops at the next double-quote (unless proceeded by \, then includes it until the next double-quote)
     |
       ;.*                # Captures any sequence of characters starting with ; (tokenized).
     |
       [^\s\[\]{}()'"`@,;]+  # Words and operators (anything that's not a special character listed)
    )
    """, re.VERBOSE)

    return [f for f in re.findall(pattern, string) if f[0] != ';']

def read_form(reader):
    # reads the token in the reader object
    character = reader.peak()
    if character == "(":
        read_list(reader)
    else:
        read_atom(reader)

def read_list(reader):
    tokens = read_forms(reader)
    for i in tokens:
        list.append(tokens[i])
        i = i+1
        if token == ")":
            break
        elif token == "EOF":
            print("ERROR")
            break

    return list


def read_atom(reader):
    # returns appropriate data type value based on given token
    token = reader.next()
    if token[0] == "\"":
        return token
    else:
        try:
            return int(token)
        except ValueError:
            return _symbol(token)

def read_str(string):
    tokens = tokenize(string)
    if len(tokens) == 0:
        raise BlankError("Blank entry") # doesn't evaluate anything because there's nothing there
    reader = Reader(tokens)
    return read_form(reader)

while True:
    input = raw_input("user> ")
    print(tokenize(input))
