

import os
import sys
import time


file_point = '/home/zhengyscn/.logstash_point'


def save_point(point):
    with open(file_point, 'w') as fd:
        fd.write(str(point))

def read_file():
    with open(file_point, 'r') as fd:
        return fd.read()

def main():

    line_num = 0
    with open('../logs/access.log', 'r') as fd:
        if os.path.exists(file_point):
            current_point = read_file()
            print current_point
            fd.seek(int(current_point), 0)
            
        print fd.read().split('\n')[0]
        #for line in fd:
        #    print line
        #    if line_num == 10:
        #        point = fd.tell()
        #        save_point(point)
        #        break
        #    line_num += 1
        #    time.sleep(1)
        
        
if __name__ == '__main__':
    main()
