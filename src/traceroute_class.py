#!/usr/bin/env python3

try:
    import src.icmplib_traceroute as icmplib_function
    import src.scapy_traceroute as scapy_function
    import src.functions as functions
    import sys
    import json
    import os
    import src.host_machine_class as host_machine
except ImportError as e:
    sys.exit("Importing error: " + str(e))

class Hop:
    """
    This is a sub-class of the traceroute to handle the details of each hop.
    Sample scapy return that nees to be handled.
    QueryAnswer
    (query=<IP  id=23970 frag=0 ttl=1 proto=udp dst=1.1.1.1 |
    <UDP  sport=15930 |>>,
    answer=<IP  version=4 ihl=5 tos=0xc0 len=56 id=25889 flags= frag=0 ttl=64 proto=icmp
    chksum=0x9124 src=192.168.1.1 dst=192.168.1.110 |
    <ICMP  type=time-exceeded code=ttl-zero-during-transit chksum=0xb931 reserved=0 length=0 unused=0 |
    <IPerror  version=4 ihl=5 tos=0x0 len=28 id=23970 flags= frag=0 ttl=1 proto=udp chksum=0x9817 src=192.168.1.110 dst=1.1.1.1 |
    <UDPerror  sport=15930 dport=domain len=8 chksum=0xfd56
    |
    >>>>)
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

    def show_all(self) -> json:
        temp_variable = {'hop':
                             {
                                 'hop id': self.hop_id,
                                 'ip version': self.ip_version,
                                 'dst': self.dst,
                                 'src': self.src,
                                 'sport': self.sport,
                                 'protocol': self.protocal
                             }
                         }
        print("This is all detail from a single hop - {}".format(temp_variable))
        return temp_variable


class HandleTraceroute:
    """
    This class file periodically checks, your home ip address and sets it as a
    machine ip address to be called for a vpn service.
    Default time = 30 mins
    """

    def __init__(self):
        self.internal_address = ['192', '10', '172']
        self.a_pipper = '169'
        self.external_address = ''
        self.hops = []
        functions.error_trapping([self.internal_address, self.external_address, self.hops])

    def strip_scapy_return(self, input_value: str) -> None:
        """
        This will strip the expected scapy traceroute return and fill a 'hop' object.
        :param input_value: Str
        :return: None
        """
        print("This is strip_scapy_return(): {}".format(input_value))
        temp = input_value.strip()
        print("Strip - {}".format(temp))

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

    def do_icmplib_traceroute(self, target='8.8.8.8') -> str:
        functions.error_trapping([target, '** do_traceroute'])
        list_hops, return_result = icmplib_function.icmplib_traceroute(target)
        for l in list_hops:
            self.hops.append(l)
        return return_result

    def split_string(self, temp) -> json:
        temp_json = {
            "id - " + temp[2][3:],
            "ttl - " + temp[4][4:],
            "protocol - " + temp[5][6:],
            "dst - " + temp[6][4:],
            "sport - " + temp[9][6:],
            "src = " + temp[10],
            "src 1= " + temp[11],
            "src 2= " + temp[12],
            "version " + temp[13][8],
            "src 3= " + temp[14],
            "src 4= " + temp[15],
            "src 5= " + temp[16],
            "src 6= " + temp[17]
        }
        # print("here: {}".format(temp_json))
        return temp_json

    def do_scapy_traceroute(self, target='8.8.8.8') -> str:
        output_list = []
        output_list = scapy_function.scapy_traceroute(target)

        print("do_scrapy_traceroute() - output_list - {}".format(output_list))
        for o in output_list:
            temp = str(o).split(" ")
            # print("the list: ".format(temp))
            return_value = self.split_string(temp)
            self.hops.append(return_value)
        return str(self.hops)

    def __print_hops(self) -> None:
        for h in self.hops:
            print(h)

    def __get_hops(self) -> json:
        output = ''
        for h in self.hops:
            output += h
        return {'hops': output}

    def __test_loop_return(self) -> json:
        return {'test': str([h for h in self.hops])}

    def set_external_ip_address(self, input_value: str) -> None:
        try:
            host_machine.set_host_environment_variables(input_value)
        except Exception as err:
            print('Error: {}'.format(err))


    def check_hops_for_external_ip_and_return(self) -> str:
        for h in self.hops:
            if self.internal_address == h:
                self.external_address = h
                return self.external_address
            else:
                pass

    def get_external_ip_address(self) -> str:
        self.external_address = host_machine.get_host_external_ip_address()
        return self.external_address

    def show_details(self) -> None:
        everything = str(self.internal_address) + \
            'The contents of self.external_address' + str(self.external_address) + \
            'The contents of all the hops' + str(self.hops) + \
            self.a_pipper
        print('This is everything...{}'.format(everything))