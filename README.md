# Python RedisQueue
[![Build Status](https://travis-ci.org/benjiao/python-redisqueue.svg?branch=master)](https://travis-ci.org/benjiao/python-redisqueue)

A simple queue implementation on top of Redis for the Python developer who needs a queue that just works!


## Installation

### Via Pip
```
pip install python-redisqueue
```

## Usage

### Import and Initialization
```
from python_redisqueue import RedisQueue
    q = RedisQueue("my_test_queue")
```

### Enqueue

```
    # Enqueue a dict() object
    q.enq({"name": "Benjie", type": "Person"})

	# Enqueue an integer
    q.enq(1)

    # Enqueue a string
    q.enq("This is a string")

```

### Dequeue
Note: `deq()` will return the item in its original `type`. (eg. Objects enqueued as dictionaries will be returned as dictionaries)
```
    results = q.deq()
```

### Purge Queue

```
    q.purge()
```


### Get Queue Length
```
    q.length()
```
