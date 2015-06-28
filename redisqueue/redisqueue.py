import json
import redis
from datetime import datetime

class RedisQueueError(Exception):
    pass

class RedisQueueConnectionError(redis.ConnectionError):
    pass

class RedisQueue:
    def __init__(self, queuename, host='localhost', port=6379, db=0):
        """
        Initializes a new instance of RedisQueue

        @param queuename A label for the queue to be created.
        @type queuename String

        @param host The hostname of the redis instance. Localhost by default
        @type host String

        @param port The port of the redis instance. Set to 6379 by default
        @type port Integer
        """

        self._queuename = "queue:%s" % queuename
        self._q = redis.StrictRedis(host=host, port=port, db=0)

    def enq(self, data):
        """
        Adds a new item into the queue.

        @param data The data to be enqueued
        @type data Mixed. Accepts int, string, or python dict()
        """

        try:
            self._q.lpush(self._queuename, data)
            return True
        except redis.ConnectionError:
            raise RedisQueueConnectionError("Cannot connect to Redis!")

    def deq(self):
        """
        Retrieves and removes the oldest item from the queue
        """

        results = self._q.rpop(self._queuename)
        return results

    def purge(self):
        """
        Removes all items from the queue
        """

        self._q.lrem(name=self._queuename, value="*", count=0)
        return True

    def deq_batch(self):
        pass

    def enq_batch(self):
        pass

if __name__ == '__main__':
    q = RedisQueue("test")
    q.enq({"testkey": "testvalue",
           "time": datetime.now()})
