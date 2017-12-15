#coding: utf-8

import json
import requests

def printJson(data):
    print json.dumps(data, indent=4)


'''经纬度
'''
def old_get_point_from_ip(ip):
    # http://api.map.baidu.com/location/ip?ip=xx.xx.xx.xx&ak=您的AK&coor=bd09ll

    #http://lbs.amap.com/api/webservice/guide/api/ipconfig/
    url = "http://api.map.baidu.com/location/ip"
    data = {'ip' : ip, 'ak' : 'odPxy2gZZ8ABQizuNkZvhUshjIwtml98', 'color' : 'bd09ll'}
    req = requests.get(url=url, params=data)
    content = req.json()
    print content['status']
    print content['content']['address']
    
    return content['content']['point'], req.ok


'''高德经纬度
'''
def get_point_from_ip(ip):
    #http://lbs.amap.com/api/webservice/guide/api/ipconfig/
    url = "http://restapi.amap.com/v3/ip" 
    data = {'ip' : ip, 'key' : 'c9556ad40fc6811432b2973ed7c1782d', 'output' : 'json'}
    req = requests.get(url=url, params=data)
    content = req.json()
    #print content['status']
    #print content['info']
    #print content['province']
    #print content['city']
    city = content['city']
    x, y = content['rectangle'].split(';')[0].split(',')
    return (x, y, city), req.ok 


if __name__ == '__main__':
    print get_point_from_ip('112.74.164.107')
    print get_point_from_ip('106.38.84.18')
