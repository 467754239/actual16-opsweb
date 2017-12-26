import time
import threading

class MyThread(threading.Thread):
    def __init__(self, signal):
        threading.Thread.__init__(self)
        self.singal = signal
 
    def run(self):
        print "%s,I will sleep ..."%self.name
        self.singal.wait()
        print "%s, I awake..." %self.name
 
if __name__ == "__main__":
    singal = threading.Event()
    for t in range(0, 100):
        thread = MyThread(singal)
        thread.start()
 
    print "main thread sleep 3 seconds... "
    time.sleep(3)
 
    singal.set()
