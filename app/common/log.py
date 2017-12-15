



def parse(filename):
    retdata = {}
    with open(filename, 'r') as fd:
        for line in fd:
            arrTmp = line.split()
            ip, status = arrTmp[0], arrTmp[8]
            print ip, status
            ip_status = (arrTmp[0], arrTmp[8])
            retdata[ip_status] = retdata.get(ip_status, 0) + 1
    return retdata



def parseStatusCount(filename):
    retdata = {}
    with open(filename, 'r') as fd:
        for line in fd:
            arrTmp = line.split()
            status = arrTmp[8]
            if status == '"-"':continue
            retdata[status] = retdata.get(status, 0) + 1
    return retdata










if __name__ == '__main__':
    filename = "/home/zhengyscn/actual16-opsweb/logs/access.log"
    #print parse(filename)
    print parseStatusCount(filename)
