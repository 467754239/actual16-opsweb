# -*- encoding: utf-8 -*-

import time
import threading

class Boy(threading.Thread):

    def __init__(self, rlock, name):
        super(Boy, self).__init__()
        self.rlock = rlock
        self.name = name

    def run(self):
        time.sleep(1)              # 确保先运行Seeker中的方法
        self.rlock.acquire()       # b
        print self.name + ': 我已经把眼睛蒙上了'
        self.rlock.notify()
        self.rlock.wait()          # c
                                   # f
        print self.name + ': 我找到你了 ~_~'
        self.rlock.notify()
        self.rlock.release()
                                       # g
        print self.name + ': 我赢了'   # h
		
		
		
class Girl(threading.Thread):

    def __init__(self, rlock, name):
        super(Girl, self).__init__()
        self.rlock = rlock
        self.name = name

    def run(self):
        self.rlock.acquire()
        self.rlock.wait()           # a    #释放对琐的占用，同时线程挂起在这里，直到被notify并重新占有琐。
                                    # d
        print self.name + ': 我已经藏好了，你快来找我吧'
        self.rlock.notify()
        self.rlock.wait()           # e
                                    # h
        self.rlock.release()
        print self.name + ': 被你找到了，哎~~~'


if __name__ == '__main__':
    rlock = threading.Condition()
    girl = Girl(rlock, 'girl')
    boy = Boy(rlock, 'boy')
    boy.start()
    girl.start()

