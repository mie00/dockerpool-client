class Docker:
    def __init__(self, pool, key):
        self.pool = pool
        self.key = key

    def stop(self):
        raise NotImplementedError()

    def execute(self, cmd, stdout=True, stderr=True, stream=False):
        raise NotImplementedError()
