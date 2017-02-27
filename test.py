import socket
import pymongo
import time
import sys

iplist = []

def ipScanner(ip):
    global iplist
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.settimeout(0.3)
    try:
        sk.connect((ip,27017))   #使用mongodb的默认端口进行尝试连接
        iplist.append(ip)
        #hdb = hdb + 1
        sk.close()
    except Exception:
        pass


def check_poc(iptset):

    global hpoc
    print '尝试连接IP地址为' + iptest + '的MongoDB数据库'
    try:
      conn = pymongo.MongoClient(iptset, 27017, socketTimeoutMS=3000)
      dbname = conn.database_names()
      if dbname:
        print "存在漏洞的Ip地址为：",iptest
        print "存在漏洞的数据库名为：",dbname
    except Exception as e:
        print '\n 不存在漏洞'

    
if __name__ == '__main__':
    start_time = time.clock()
    
    ip_input = raw_input("输入要扫描的IP地址段的网络地址:")
    ip0 = ip_input.split('.')
    for i in range(1,255):
        ip_addr =  ip0[0]+'.'+ip0[1]+'.'+ip0[2]+'.'+str(i)
        ipScanner(ip_addr)

    for iptest in iplist:
        check_poc(iptest)
    
    end_time = time.clock()
    #print "共有[",hdb,']个IP地址有该数据库。其中有[',hpoc,']个数据库存在未授权访问漏洞’
    print "共用时：" ,(end_time - start_time)

