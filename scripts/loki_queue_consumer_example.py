import sys
from loki.broker.queue import Queue, RedisQueueEngine


host = sys.argv[1]
port = sys.argv[2]
redis_engine = RedisQueueEngine(host,port)
input_queue = Queue('examples::data_consumer::input', redis_engine)
output_queue = Queue('examples::data_consumer::output', redis_engine)
while True:
    data = input_queue.rpop(blocking=True)
    print "From input queue:",data
    sys.stdout.flush()
    output_queue.lpush(data)
    
