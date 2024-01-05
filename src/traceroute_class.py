#!/usr/bin/env python3

try:
    import src.functions as functions
    import sys
    import json
    import os
except ImportError as e:
    sys.exit("Importing error: " + str(e))


class HandleTraceroute:
    """
    This class file holds the framework of a traceroute return. The sub_class is a number of "Hop" objects.
    """

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

    def __init__(self):
        self.internal_address = ['192', '10', '172']
        self.a_pipper = '169'
        self.external_address = ''
        # this needs a number of hop instances - not sure correct methodology
        # 1
        self.hops = [self.Hop()]
        # 2
        self.temp_hops = HandleTraceroute.Hop()
        self.a_number_of_hops = [self.temp_hops]
        # functions.error_trapping(
        #    ['initiating trace object - ', self.internal_address, self.external_address, self.hops
        #    ])

    def get_internal_address(self) -> list:
        return self.internal_address

    def get_a_pipper(self) -> str:
        return self.a_pipper

    def set_external_address(self, value: str) -> None:
        self.external_address = value

    def get_external_address(self) -> str:
        return self.external_address

    def append_hops(self, value: Hop) -> None:
        # functions.error_trapping(['append_hops() -', str(value.dst), ' - src', str(value.src)])
        self.hops.append(value)

    def pop_hops(self) -> json:
        print("appending pop_hops() - {} - {}".format(self.hops.count, self.hops.pop()))
        return {'popping hops() count - ': self.hops.count}

    def is_external_address_empty(self) -> bool:
        if not self.external_address:
            return False
        else:
            return True

    def check_ip_address_if_external(self, input_var) -> bool:
        if input_var in self.internal_address:
            return False
        else:
            return True

    def get_hops(self) -> json:
        return {'hops': self.a_number_of_hops}

    def __test_loop_return(self) -> json:
        return {'test': str([h for h in self.hops])}

    def check_hops_for_external_ip_and_return(self) -> str:
        for h in self.hops:
            if self.internal_address == h:
                self.external_address = str(h)
                temp_variable = str(h).split('.')[0]
                return temp_variable
            else:
                pass

    def show_details(self) -> json:
        everything = {
            'internal_addresses': self.internal_address,
            'a_pipper ': self.a_pipper,
            'external_address': self.external_address,
            'hops': self.get_hops()
        }
        print('This is everything...{}'.format(everything))
        return everything
