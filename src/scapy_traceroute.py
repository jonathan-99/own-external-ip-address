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


def scapy_traceroute(target='1.1.1.1'):
    DNS_variable = '/DNS(qd=DNSQR(qname="www.google.com"))'
    result, unans = traceroute(target, nofilter=1, l4=UDP(sport=RandShort()))
    return result, unans

if __name__ == '__main__':
    scapy_traceroute()