# Holds functions for printing tokens

def pr_str(token):
    # takes tokens and returns a string of it
    if type(token) == sym:
        return "token"

    if type(token) == int:
        return "token"

    if type(token) == list:
        for i in range len(token):
            list.append token[i]
            i++
        return (list)
