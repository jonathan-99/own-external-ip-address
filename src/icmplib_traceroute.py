#!/usr/bin/env python3

"""
This was developed to use the icmplib library but failed to function.
"""

try:
    from icmplib import traceroute
    import src.scapy_traceroute as scapy_function
    import src.functions as functions
    import sys
    import json
    import os
    import src.host_machine_class
except ImportError as e:
    sys.exit("Importing error: " + str(e))


def icmplib_traceroute(target='1.1.1.1'):
    # execute
    hops = [] # this is being used for returning the class hops
    hop = traceroute(target)
    functions.error_trapping(['this bit', hop])
    last_distance = 0
    for h in hop:
        functions.error_trapping(['noe here', h, last_distance, h.distance])
        if last_distance + 1 != h.distance:
            print('gateways ae not responding')
        hops.append(h)
        last_distance = h.distance
    return hops, hop


if __name__ == '__main__':
    icmplib_traceroute()