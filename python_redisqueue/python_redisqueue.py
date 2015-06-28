import json
import redis
from datetime import datetime


class RedisQueueError(Exception):
    pass


class RedisQueueBadDataError(RedisQueueError):
    pass


class RedisQueue:
    def __init__(self, name, host='localhost', port=6379, db=0):
        """
        Initializes a new instance of RedisQueue

        @param queuename A label for the queue to be created.
        @type queuename String

        @param host The hostname of the redis instance. Localhost by default
        @type host String

        @param port The port of the redis instance. Set to 6379 by default
        @type port Integer
        """

        self._queuename = "queue:%s" % name
        self._q = redis.StrictRedis(host=host, port=port, db=0)

    def enq(self, data):
        """
        Adds a new item into the queue.

        @param data The data to be enqueued
        @type data Mixed. Accepts int, string, or python dict()
        """

        data_type = type(data)

        try:
            if data_type is str:
                data_json = json.dumps({"type": "str", "body": str(data)})
            elif data_type is int:
                data_json = json.dumps({"type": "int", "body": str(data)})
            elif data_type is dict:
                data_json = json.dumps({"type": "dict", "body": data})
            else:
               raise RedisQueueError(("Data type cannot be encoded: %s. " +
                                      "Please use <type 'int'>, <type 'str'> " +
                                      "or <type 'dict'> instead") % data_type)

            self._q.lpush(self._queuename, data_json)
            return True

        except RedisQueueError:
            raise
        except redis.ConnectionError, e:
            raise RedisQueueError("Cannot connect to Redis! %s" %
                                  str(type(e))+str(e))
        except Exception, e:
            raise RedisQueueError("Unexpected error: %s" %
                                  str(type(e)) + str(e))

    def deq(self):
        """
        Retrieves and removes the oldest item from the queue
        """

        try:
            results = self._q.rpop(self._queuename)
            results_dict = json.loads(results)

            try:
                data_type = results_dict["type"]
            except KeyError, e:
                raise RedisQueueBadDataError("Bad data format! ('type' key is missing)")

            if data_type == "str":
                return str(results_dict["body"])
            elif data_type == "int":
                return int(results_dict["body"])
            elif data_type == "dict":
                return results_dict["body"]
            else:
                raise RedisQueueError("Unknown data type saved: %s" %
                                      results_dict.get("type"))

        except RedisQueueError:
            raise

        except redis.ConnectionError, e:
            raise RedisQueueError("Cannot connect to Redis! %s" %
                                  str(type(e))+str(e))
        except Exception, e:
            raise RedisQueueError("Unexpected error: %s" %
                                  str(type(e)) + str(e))

    def length(self):
        try:
            results = self._q.llen(self._queuename)
            return results
        except redis.ConnectionError, e:
            raise RedisQueueError("Cannot connect to Redis! %s" %
                                  str(type(e))+str(e))
        except Exception, e:
            raise RedisQueueError("Unexpected error: %s" % str(type(e)) + str(e))

    def purge(self):
        """
        Removes all items from the queue
        """

        self._q.delete(self._queuename)
        return True

    def deq_batch(self):
        raise RedisQueueError("Method not implemented yet!")

    def enq_batch(self):
        raise RedisQueueError("Method not implemented yet!")

if __name__ == '__main__':
    q = RedisQueue("test")
    results = q.deq()

    q.enq({"testkey": "testvalue",
           "time": datetime.now()})
