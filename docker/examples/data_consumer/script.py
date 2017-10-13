from loki.broker.queue import Queue, RedisQueueEngine

redis_engine = RedisQueueEngine('redis',6379)
input_queue = Queue('examples::data_consumer::input', redis_engine)
output_queue = Queue('examples::data_consumer::output', redis_engine)
while True:
    data = input_queue.brpop()
    print "From input queue:",data
    output_queue.lpush(data)
