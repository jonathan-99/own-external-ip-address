#!/usr/bin/env python3

try:
    import src.functions as functions
    import sys
    import os
    import json
    import logging
except ImportError as e:
    import json
    import logging
    import src.functions as functions
    logging.error("Importing error: " + str(e))


class Hop:
    """
    This is a sub_class of the traceroute to handle the details of each hop.
    Sample scapy return that needs to be handled.
    QueryAnswer
    (query=<IP  id=23970 frag=0 ttl=1 proto=udp dst=1.1.1.1 |
    UDP  sport=15930 |>>,
    answer=<IP  version=4 ihl=5 tos=0xc0 len=56 id=25889 flags= frag=0 ttl=64 proto=icmp
    chksum=0x9124 src=192.168.1.1 dst=192.168.1.110 |
    ICMP  type=time-exceeded code=ttl-zero-during-transit chksum=0xb931 reserved=0 length=0 unused=0 |
    IPerror
        version=4 ihl=5 tos=0x0 len=28 id=23970 flags=
        frag=0 ttl=1 proto=udp chksum=0x9817
        src=192.168.1.110 dst=1.1.1.1 |
    UDPerror  sport=15930 dport=domain len=8 chksum=0xfd56
    """

    def __init__(self):
        self.hop_id = ""
        self.sport = ""
        self.dst = ""
        self.ip_version = ""
        self.ttl = ""
        self.protocol = ""
        self.src = ""

    def fill_single_hope_line_into_object(self, input_line):
        logging.debug(f"fill_single_hop_line_into_object()")
        if 'QueryAnswer' in input_line:
            line = input_line.split(' ')
            # print(f"l here is {l} - {l['id=']}")
            self.add_hop_id(line['id='])  # Replace with actual hop ID
            self.add_sport(line['sport='])  # Replace with actual sport
            self.add_dst(line['dst='])  # Replace with actual destination
            self.add_ip_version(line['version='])  # Replace with actual IP version
            self.add_ttl(line['ttl='])  # Replace with actual TTL
            self.add_protocol(line['proto='])  # Replace with actual protocol
            self.add_src(line['src='])  # Replace with actual source
        print(f" show all hop - {self.show_all()}")
        return self

    def add_hop_id(self, value) -> None:
        self.hop_id = str(value)

    def add_sport(self, value) -> None:
        self.sport = str(value)

    def add_dst(self, value) -> None:
        self.dst = str(value)

    def add_ip_version(self, value) -> None:
        self.ip_version = str(value)

    def add_ttl(self, value) -> None:
        self.ttl = str(value)

    def add_protocol(self, value) -> None:
        self.protocol = str(value)

    def add_src(self, value) -> None:
        self.src = str(value)

    def get_ip_address(self, direction='dst') -> str:
        if direction == 'dst':
            return_value = (str(self.dst).split('.'))[0]
        elif direction == 'src':
            return_value = (str(self.src).split('.'))[0]
        else:
            return_value = 'get_ip_address() - error'
        functions.error_trapping(['splitting hop address', return_value])
        return return_value

    def get_hops_object(self):
        return self

    def show_all(self) -> json:
        return {'hop':
                {
                    'hop id': self.hop_id,
                    'ip version': self.ip_version,
                    'dst': self.dst,
                    'src': self.src,
                    'sport': self.sport,
                    'protocol': self.protocol
                }}
