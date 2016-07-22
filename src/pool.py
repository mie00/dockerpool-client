import uuid
import threading

from .dockerwrapper import Docker

class Pool:
    def __init__(self, pools, key):
        self.pools = pools
        self.key = keys

    def refresh(self):
        raise NotImplementedError()

    def get(self, key=None):
        if key == None:
            key = self.get_new()
        return Docker(self, key)

    def get_new(self):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()
