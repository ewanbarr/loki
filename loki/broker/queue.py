import redis

class RedisQueueEngine(object):
    def __init__(self, host, port):
        self.client = redis.StrictRedis(host=host, port=port, db=0)

    def lpop(self, name):
        return self.client.lpop(name)

    def rpop(self, name):
        return self.client.rpop(name)

    def lpush(self, name, value):
        return self.client.lpush(name, value)

    def rpush(self, name, value):
        return self.client.rpush(name, value)


class Queue(object):
    def __init__(self, queue_name, engine):
        self.queue_name = queue_name
        self.engine = engine

    def lpop(self):
        return self.engine.lpop(self.queue_name)

    def rpop(self):
        return self.engine.rpop(self.queue_name)

    def lpush(self, value):
        return self.engine.lpush(self.queue_name, value)

    def rpush(self, value):
        return self.engine.rpush(self.queue_name, value)

