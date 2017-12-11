# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import sys
import time
import socket
import json
import logging
import requests
import subprocess

import psutil

reload(sys)
sys.setdefaultencoding('utf-8')

def get_hostname():
    return socket.gethostname()


def get_mem_info():
    fd = open('/proc/meminfo', 'r')
    mem_total = fd.readline().split()[1]
    fd.close()
    return {'mem_total': int(mem_total) / 1024}


def get_cpu_info():
    cpu_info = {'cpu_num' : 0, 'cpu_model' : None}
    with open('/proc/cpuinfo', 'r') as f:
        for line in f:
            if line.startswith('processor'):
                cpu_info['cpu_num'] += 1
            elif line.startswith('model name'):
                cpu_info['cpu_model'] = line.split(':')[1].strip()
    return cpu_info


def get_device_info():
    ret = {'public_ip' : '', 'private_ip' : ''}
    addinfo = psutil.net_if_addrs()
    ret['private_ip'] = addinfo['eth0'][0].address
    return ret

def get_disk_info():
    deviceinfo = [ obj.mountpoint  for obj in psutil.disk_partitions() ]
    disk_total = sum([ psutil.disk_usage(device).total / 1024 / 1024 / 1024  for device in deviceinfo ])
    return {"disk" : disk_total}

def get_os_version():
    pass

def get_time():
    return int(time.time())

def execute(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return p.stdout.read()

def send(data):
    url = 'http://112.74.164.107:8000/assets'
    req = requests.post(url=url, data=data)
    print req.status_code
    print req.text

def run():
    data = {}
    data['hostname'] = get_hostname()
    data.update(get_mem_info())
    data.update(get_cpu_info())
    data.update(get_device_info())
    data.update(get_disk_info())
    print json.dumps(data, indent=4)
    
    send(data)

if __name__ == '__main__':
    run()
