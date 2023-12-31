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
        "id": temp[7][3:],
        "ttl": temp[10][4:],
        "protocol": temp[11][6:],
        "dst": temp[14][4:],
        "src": temp[13][4:],
        "version": temp[3][8]
    }
    return temp_json

def re_order_hops(input_list: list) -> list:
    """
    Some hops are recorded in random orders: desired outcome - >
     - dst, id, protocol, version, src, ttl
    :param input_list:
    :return:
    """
    temp_dst = ''
    temp_id = ''
    temp_protocol = ''
    temp_version = ''
    temp_src = ''
    temp_ttl = ''
    output_list = []

    for i in input_list:
        temp_dst = i['dst']
        temp_id = i['id']
        temp_protocol = i['protocol']
        temp_version = i['version']
        temp_src = i['src']
        temp_ttl = i['ttl']
        output_list.append(
            {
                'dst': temp_dst,
                'id': temp_id,
                'protocol': temp_protocol,
                'version': temp_version,
                'src': temp_src,
                'ttl': temp_ttl
            }
        )
    print("re_order_hops() - ".format(output_list))

    # needs to return a json
    return output_list

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
        #  print("json return of items - {}".format(return_json))
        #  returns this ... {'protocol - icmp', 'id - 13061', 'version 4', 'src = 192.168.1.1', 'ttl - 64', 'dst - 192.168.1.110'}
        return_list.append(return_json)
    return_list = re_order_hops(return_list)
    return return_list

if __name__ == '__main__':
    scapy_traceroute()