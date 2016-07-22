from .pool import Pool

class Pools:
    def __init__(self, server='http://localhost/'):
        self.server = server

    def refresh(self):
        raise NotImplementedError()

    def create(self, *args, **kwargs):
        raise NotImplementedError()

    def get(self, *args, **kwargs):
        raise NotImplementedError()

    def get_by_key(self, key):
        return Pool(self, key)
