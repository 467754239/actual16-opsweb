#--*--coding: utf-8--*--

import redis



class Redis(object):

    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db = db
        self.prodcons_queue = 'task:prodcons:queue'
        self.pubsub_channel = 'task:pubsub:channel'
        self.conn = self.connect()

    def connect(self):
        self.conn = redis.StrictRedis(host=self.host, port=self.port, db=self.db)
        return self.conn


    # push element to queue
    def push(self, element):
        self.conn.lpush(self.prodcons_queue, element)

    # subscribe 订阅
    # subscribe channel
    def publish(self, element):
        pubsub = self.conn.pubsub()
        pubsub.subscribe(self.pubsub_channel)
        self.conn.publish(self.pubsub_channel, element)







if __name__ == '__main__':
    '''
        LRANGE "task:prodcons:queue" 0 -1
        SUBSCRIBE  'task:pubsub:channel'
    '''
    pass
