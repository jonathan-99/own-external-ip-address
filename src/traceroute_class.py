#!/usr/bin/env python3

try:
    import src.functions as functions
    import sys
    import json
    import os
    import logging
    import src.hop_class as hop
    import xml.etree.ElementTree as ET
    import xml
except ImportError as e:
    logging.error("Importing error: " + str(e))


class HandleTraceroute:
    """
    This class file holds the framework of a traceroute return. The sub_class is a number of "Hop" objects.
    """

    def __init__(self):
        self.internal_address = ['192', '10', '172']
        self.a_pipper = '169'
        self.external_address = ''
        # this needs a number of hop instances - not sure correct methodology
        # 1
        self.hops = []

    def is_empty(self) -> bool:
        if (not self.hops):
            return True
        else:
            return False

    def reformat_xml(self, input_code: str) -> xml:
        ip_attributes = ["id", "frag", "ttl", "proto", "dst"]
        udp_attributes = ["sport"]
        answer_attribute =['ip', 'version', 'id', 'flags', 'ttl', 'proto', 'src', 'dst']
        icmp_attribute = ['type', 'code', 'chksum', 'reserved', 'length', 'unused']
        ip_error_attribute = ['version', 'ihl', 'tos', 'len', 'id', 'flags', 'frag', 'ttl', 'proto', 'chksum', 'src', 'dst']
        udp_error_attribute = ['sport', 'dport', 'len', 'chksum']

        # need to extract the other attributes which are embedded. the top level "query" is done, now all within answer

        # Split the input into relevant parts
        udp_start = input_code.find("|<UDP")
        icmp_start = input_code.find("|<ICMP")
        IPerror_start = input_code.find("|IPerror")
        UDPerror_start = input_code.find("UDPerror")
        the_end = input_code.find("|>>>")
        udp_end = input_code.find(">", udp_start) + 1

        # Split the input into relevant parts
        ip_part = input_code[:udp_start]
        udp_part = input_code[udp_start:udp_end]
        icmp_part = input_code[icmp_start:IPerror_start - 2]
        UDPerror_part = input_code[UDPerror_start:the_end - 2]

        # Extract attributes for <IP>
        ip_attributes_dict = {}
        for item in ip_part.split(" ")[1:]:
            if "=" in item:
                attr, value = item.strip().split("=")
                ip_attributes_dict[attr] = value.strip()

        # Extract attributes for <UDP>
        udp_attributes_dict = {}
        for item in udp_part.split(" ")[1:]:
            if "=" in item:
                attr, value = item.strip().split("=")
                udp_attributes_dict[attr] = value.strip()

        # Extract attributes for <ICMP>
        icmp_attributes_dict = {}
        for item in icmp_part.split(" ")[1:]:
            if "=" in item:
                attr, value = item.strip().split("=")
                icmp_attributes_dict[attr] = value.strip()

        # Extract attributes for <UDPerror>
        UDPerror_attributes_dict = {}
        for item in UDPerror_part.split(" ")[1:]:
            if "=" in item:
                attr, value = item.strip().split("=")
                UDPerror_attributes_dict[attr] = value.strip()

        # Create an XML structure
        root = ET.Element("QueryAnswer")

        ip_element = ET.SubElement(root, "IP", ip_attributes_dict)
        udp_element = ET.SubElement(ip_element, "UDP", udp_attributes_dict)
        xml_string = ET.tostring(root, encoding="unicode", method="xml")
        print(f"this is the xml - {xml_string}")

        return xml_string

    def translate_string_into_xml(self, input_code: str):
        result_string = input_code[input_code.find('=') + 1:]
        new_xml = self.reformat_xml(result_string)

    def process_traceroute_return(self, return_code: str) -> None:  # this needs to return a trace object
        logging.debug("process_traceroute_return()")
        self.translate_string_into_xml(return_code)
        hop_object = hop.Hop()
        for element in return_code.split('|'):
            print(f"this is the line - {type(element)} - {element}")
            hop_object.fill_single_hope_line_into_object(element)
            self.hops.append(hop_object)
        print(f"This is process_traceroute_return() {self.show_details()}")
        return

    def get_internal_address(self) -> list:
        return self.internal_address

    def get_a_pipper(self) -> str:
        return self.a_pipper

    def set_external_address(self, value: str) -> None:
        self.external_address = value

    def get_external_address(self) -> str:
        return self.external_address

    def append_hops(self, number: int, value: dict) -> None:
        logging.debug(f'append_hops() - {number} - {value}')
        input_data = {
            "Hop Number": number,
            "Hop Info": {
                'src': value['src'],
                'dst': value['dst'],
                'ttl': value['ttl'],
                'proto': value['proto']
            }
        }
        self.hops.append(input_data)

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

    def return_first_external_hop(self) -> str:
        for a in self.hops:
            logging.debug(f'return_first_external_hop {a}')
            print(f'Hop by hop {a}')
            temp = a['Hop Info']['src'].split('.')
            print(f'temp - {temp}')
            #  Hop by hop {'Hop Number': 2, 'Hop Info': {'src': '192.168.83.251', 'dst': '10.7.5.67', 'ttl': 63, 'proto': 1}} - {'Hop Number': 2, 'Hop Info': {'src': '192.168.83.251', 'dst': '10.7.5.67', 'ttl': 63, 'proto': 1}}
            if a in self.internal_address:
                pass
            else:
                self.set_external_address(a)
                logging.debug(f'We have matched an external ip address :{a}')
        return self.get_external_address()