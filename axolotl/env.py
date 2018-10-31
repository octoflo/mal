# Functions to set up the environment to store define functions and varibles

class Env():

    def __init__(self, outer=None, exprs=None, params=None):
        """The outer environment will always be the repl_env. Inner would be the local environments.
        It can also take parameters (params) and the script (exprs) if the token is a function."""

        self.data = {}
        self.outer = outer

        if exprs:
            # If a function program is given
            for i in range(len(exprs)):
                # go through each token and look if there's an & symbol (for if statement)
                if exprs[i] == "&":
                    self.data[exprs[i+1]] = exprs[i:]
                    break
                else:
                    self.data[exprs[i]] = exprs[i]

    def set(self, key, value):
        # add data to dictionary environment
        self.data[key] = value
        return value

    def find(self, key):
        # finding what dictionary the key is in (inner or outer environment)
        if key in self.data:
            return self.datas
        elif self.outer:
            return self.outer.find(key)
        else:
            return None

    def get(self, key):
        # returning the key's value based on it's dictionary placement
        env = self.find(key)
        if env:
            return env[key]
        else:
            raise Exception("'" + key + "' not found")
