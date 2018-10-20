class Env():
    def __init__(self, outer=None):
        # inner = local_env, outer = repl_env
        self.data = {}
        self.outer = outer

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
