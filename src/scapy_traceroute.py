#!/usr/bin/env python3

"""
This was used due to installation / using issues with icmplib. This was designed on Windows but executed on linux.
"""

try:
    from scapy.layers.inet import *
    import src.functions as functions
    import sys
    import json
    import os
    import src.host_machine_class
    import src.hop_class as hop
    import src.traceroute_class as trace
    import logging
except ImportError as e:
    import logging
    logging.error("Importing error: (scapy_traceroute.py)" + str(e))
    sys.exit()
except Exception as err:
    import logging
    logging.error(f"This is a wider error catch - {err}")


def scapy_traceroute(target='1.1.1.1'):  # tbd
    # dns_variable = '/DNS(qd=DNSQR(qname="www.google.com"))'
    result, unans = traceroute(target, nofilter=1, l4=UDP(sport=RandShort()))
    print(f"uname - {type(unans)} - {unans}")
    trace_object = trace.HandleTraceroute()
    for r in result:
        print(f"Result r type {type(r)} - {r}")
        trace_object.process_traceroute_return(str(r))
        trace_object.show_details()
    return  # tbd


if __name__ == '__main__':
    logging.debug(str(scapy_traceroute("1.1.1.1")))
