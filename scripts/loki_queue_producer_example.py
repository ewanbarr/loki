import sys
import time
from loki.broker.queue import Queue, RedisQueueEngine

host = sys.argv[1]
port = sys.argv[2]
print "Connecting to Redis"
redis_engine = RedisQueueEngine(host,port)
input_queue = Queue('examples::data_consumer::input', redis_engine)
ii = 0
while True:
    data = "Message no: {}".format(ii)
    print "Pushing: '{}' to queue '{}'".format(data,'examples::data_consumer::input')
    input_queue.lpush(data)
    ii+=1
    time.sleep(5)
    
