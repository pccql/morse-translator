from interfaces.DatabaseInterface import DatabaseInterface


class RedisAdapter(DatabaseInterface):
    def __init__(self, redis_client):
        self.client = redis_client

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value):
        return self.client.set(key, value)

    def keys(self):
        return self.client.keys()
