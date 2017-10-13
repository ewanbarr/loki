import sys
from loki.broker.queue import Queue, RedisQueueEngine

host = sys.argv[1]
port = sys.argv[2]
redis_engine = RedisQueueEngine(host,port)
input_queue = Queue('examples::data_consumer::input', redis_engine)
ii = 0
while True:
    data = "Message no: {}".format(ii)
    input_queue.lpush(data)
    ii+=1
    
