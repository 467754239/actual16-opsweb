#coding: utf-8

import time
import redis
import random

from flask import Flask
from flask import redirect


app = Flask(__name__)


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

    def pop(self):
        while True:
            task = self.rcon.blpop(self.queue,0)[1]
            print task
            time.sleep(1)

    # subscribe 订阅
    # subscribe channel
    def publish(self, element):
        pubsub = self.conn.pubsub()
        pubsub.subscribe(self.pubsub_channel)
        self.conn.publish(self.pubsub_channel, element)





@app.route('/')
def index():
    html = """
    <br>
    <center><h3>Redis Message Queue</h3>
    <br>
    <a href="/prodcons">生产消费者模式</a>
    <br>
    <br>
    <a href="/pubsub">发布订阅者模式</a>
    </center>
    """
    return html


@app.route('/prodcons')
def prodcons():
    task= random.randrange(10)
    redisConn.push(task)
    return redirect('/')


@app.route('/pubsub')
def pubsub():
    task= random.randrange(10)
    redisConn.publish(task)
    return redirect('/')

if __name__ == '__main__':
    redisConn = Redis('127.0.0.1', 6379, 0) 
    app.run(host='0.0.0.0', port=9999, debug=True)

