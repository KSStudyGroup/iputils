#!/bin/env python
#coding:utf-8
'''
这是一个IP工具包，包含一些用于IP计算工具。
可以方便地实现IP地址的各种转换要求。
'''

import socket,struct

'''
@ip_start  IP起始地址
@ip_end    IP结束地址
@return  ['192.168.1.1', '192.168.1.2'] 包含在IP起始地址和结束地址之间的所有IP地址的列表
'''
def ip_list(ip_start, ip_end):
    res = []
    ip_start_n = 0
    ip_end_n = 0
    try:
        ip_start_n = struct.unpack('!I', socket.inet_aton(ip_start))[0]
        ip_end_n = struct.unpack('!I', socket.inet_aton(ip_end))[0]
    except Exception,e:
        print e
    for i in xrange(ip_start_n, ip_end_n):
        res.append(socket.inet_ntoa(struct.pack('!I', i)))
    return res

'''
@ip_start  IP起始地址
@ip_end    IP结束地址
@return    192.168.0.1/24 之类的IP表示法
'''
def to_range(ip_start, ip_end):
    ip_start_n = 0
    ip_end_n = 0
    try:
        ip_start_n = struct.unpack('!I', socket.inet_aton(ip_start))[0]
        ip_end_n = struct.unpack('!I', socket.inet_aton(ip_end))[0]
    except Exception,e:
        print e
    tmp = ip_start_n ^ ip_end_n
    zero_num = 0
    while tmp != 0:
        tmp = (tmp>>1)
        zero_num = zero_num + 1
    zero_num = 32 - zero_num
    return '%s/%d' % (ip_start, zero_num)

'''
@ip_ranges 待排序的ip range列表。ip range 格式为：192.168.0.1/24
@return    范围从小到达排序的 ip range.
'''
def range_sort(ip_ranges):
    range_dict = {}
    res = []
    for i in ip_ranges:
        ip, mask = i.split('/', 2)
        if range_dict.has_key(mask):
            range_dict[mask].append(i)
        else:
            range_dict[mask] = []
            range_dict[mask].append(i)
    for k,v in sorted(range_dict.iteritems(), key=lambda d:int(d[0]), reverse=True):
        res.extend(v)
    return res

if __name__ == '__main__':
    import sys
    #print ip_list(sys.argv[1], sys.argv[2])
    print to_range(sys.argv[1], sys.argv[2])
    #print range_sort(['192.168.0.1/32', '192.168.0.1/24'])
