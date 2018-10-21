class Env():
    def __init__(self, outer=None, binds=None, exprs=None):
        # inner = local_env, outer = repl_env
        self.data = {}
        self.outer = outer

        if binds:
            for i in range(len(binds)):
                if binds[i] == "&":
                    # for if/and statements
                    self.data[binds[i+1]] = exprs[i:]
                    break
                else:
                    self.data[binds[i]] = exprs[i]

    def set(self, key, value):
        # add data to dictionary
        self.data[key] = value
        return value

    def find(self, key):
        # finding what dictionary the key is in (inner or outer)
        if key in self.data:
            return self.data
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
