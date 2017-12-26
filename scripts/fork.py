
import os
import time


current_pid = os.getpid()
print "current process id: ", current_pid

pid = os.fork()
print "fork pid: ", pid
if pid == 0:
    time.sleep(3)
    print 'child process.'
else:
    wait_pid, status = os.wait()
    print "wait_pid:%s, status:%s." % (wait_pid, status)

    print 'parent process.'
