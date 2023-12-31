#!/usr/bin/env python3

"""
This was used due to installation / using issues with icmplib. This was desgined on Windows but executed on linux.
"""

try:
    from scapy.layers.inet import *
    import src.functions as functions
    import sys
    import json
    import os
    import src.host_machine_class
except ImportError as e:
    sys.exit("Importing error: " + str(e))

def answer(temp: list) -> json:
    temp_json = {
        "id - " + temp[7][3:],
        "ttl - " + temp[10][4:],
        "protocol - " + temp[11][6:],
        "dst - " + temp[14][4:],
        "src = " + temp[13][4:],
        "version " + temp[3][8]
    }
    return temp_json
def scapy_traceroute(target='1.1.1.1') -> list:
    return_list = []
    DNS_variable = '/DNS(qd=DNSQR(qname="www.google.com"))'
    result, unans = traceroute(target, nofilter=1, l4=UDP(sport=RandShort()))
    # i need to understand the format of the return, is it an object?
    for r in result:
        # print("raw scapy return: {} - {}".format(type(r), r))
        temp = str(r).split(',')
        # print("splitting temp for answer - {} - {}".format(type(temp[1]), temp[1]))
        t = str(temp[1]).split(' ') # this makes it a list
        # print("sub-t: {} - {}".format(type(t), t))
        return_json = answer(t)
        print("json return of items - {}".format(return_json))
        return_list.append(r)
    return return_list

if __name__ == '__main__':
    scapy_traceroute()