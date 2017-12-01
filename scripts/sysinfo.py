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


def get_mem_info(noBufferCache=True):
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
    dev_white = ['/dev/xvda']

    cmd = '''sudo fdisk -l | grep "磁盘" | egrep -v "gpt|dos|磁盘标识符"'''
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    read_data = p.stdout.read()

    for dev_line  in read_data.strip().split('\n'):
        if dev_line.startswith('WARNING'):
            continue
        break

    return {}

def get_manufacturer():
    # 制造商信息
    ret = {}
    cmd = """/usr/sbin/dmidecode | grep -A6 'System Information'"""
    data = execute(cmd)
    for line in data.split('\n'):
        if 'Manufacturer' in line:
            ret['manufacturers'] = line.split(':')[1].lstrip()
        elif 'Product Name' in line:
            ret['server_type'] = line.split(':')[1].lstrip()
        elif 'Serial Number' in line:
            ret['sn'] = line.split(':')[1].lstrip()
        elif 'UUID' in line:
            ret['uuid'] = line.split(':')[1].lstrip()
    return ret


def get_rel_data():
    # 出厂日期
    cmd = """/usr/sbin/dmidecode | grep -i release"""
    data = execute(cmd)
    date = data.split()[-1].replace('/','-')
    return {'leave_date' : date}

def get_os_version():
    pass

def get_time():
    return int(time.time())

def format(num):
    unit = {'K' : 1, 'M' : 2 ** 10, 'G' : 2 ** 20, 'T' : 2 ** 30}  
    for k, v in unit.items():
        t = float(num) / v
        if t >= 1 and t < 1024:
            return '%s%s' % (round(t, 2), k)
    return

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
    data.update(get_manufacturer())
    data.update(get_rel_data())
    print json.dumps(data, indent=4)
    
    #send(data)

if __name__ == '__main__':
    run()
