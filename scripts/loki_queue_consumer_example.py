import sys
from loki.broker.queue import Queue, RedisQueueEngine

redis_engine = RedisQueueEngine('127.0.0.1',6379)
input_queue = Queue('examples::data_consumer::input', redis_engine)
output_queue = Queue('examples::data_consumer::output', redis_engine)
while True:
    data = input_queue.rpop(blocking=True)
    print "From input queue:",data
    sys.stdout.flush()
    output_queue.lpush(data)
    