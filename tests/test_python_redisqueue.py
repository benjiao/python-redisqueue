import uuid
from unittest import TestCase

import python_redisqueue


class BasicTests(TestCase):

    def setUp(self):
        """
        Generate a queuename for this test (with random uuid)
        """
        self.queuename = "redisqueuetest:%s" % uuid.uuid4()
        self.queue = python_redisqueue.RedisQueue(self.queuename)

    def test_length_on_empty(self):
        """
        length() must return 0 if queue is empty/not yet in redis
        """

        l = self.queue.length()
        self.assertEqual(0, l)

    def test_dequeue_on_empty(self):
        """
        deq() must return None if no item has been dequeued
        """
        r = self.queue.deq()
        self.assertEqual(None, r)

    def test_enqueue_int(self):
        """
        Enqueueing and dequeueing an integer must return <type 'int'> type
        """

        self.queue.enq(1)

        l = self.queue.length()
        self.assertEqual(1, l)

        r = self.queue.deq()
        self.assertEqual(int, type(r))
        self.assertEqual(1, r)

    def test_enqueue_string(self):
        """
        Enqueueing and dequeueing a string must return <type 'str'> type
        """
        self.queue.enq("Test String")

        l = self.queue.length()
        self.assertEqual(1, l)

        r = self.queue.deq()
        self.assertEqual(str, type(r))
        self.assertEqual("Test String", r)

    def test_enqueue_dict(self):
        """
        Enqueueing and dequeueing a python dict() object must return <type 'dict'> type
        """
        d = {"Test Key 1": "Test Value 1",
             "Test Key 2": "Test Value 2"}

        self.queue.enq(d)

        l = self.queue.length()
        self.assertEqual(1, l)

        r = self.queue.deq()
        self.assertEqual(dict, type(r))
        self.assertEqual(d, r)

    def test_ordering(self):
        """
        Order must be preserved. Should strictly follow first-in first-out.
        """
        self.queue.enq("First")
        self.queue.enq("Second")
        self.queue.enq("Third")

        self.assertEqual("First", self.queue.deq())
        self.assertEqual("Second", self.queue.deq())
        self.assertEqual("Third", self.queue.deq())

    def test_purge(self):
        """
        purge() must empty a queue
        """

        self.queue.enq("First")
        self.queue.enq("Second")
        self.queue.enq("Third")

        l = self.queue.length()
        self.assertEqual(3, l)

        self.queue.purge()

        l = self.queue.length()
        self.assertEqual(0, l)
