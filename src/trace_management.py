#!/usr/bin/env python3

try:
    import src.icmplib_traceroute as icmplib_function
    import src.scapy_traceroute as scapy_function
    import src.functions as functions
    import src.traceroute_class as trace_class
    import sys
    import json
    import os
    import src.host_machine_class as host_machine
except ImportError as e:
    sys.exit("Importing error: " + str(e))


def strip_scapy_return(input_value: str) -> None:
    """
    This will strip the expected scapy traceroute return and fill a 'hop' object.
    :param input_value: Str
    :return: None
    """
    print("This is strip_scapy_return(): {}".format(input_value))
    temp = input_value.strip()
    print("Strip - {}".format(temp))


def do_icmplib_traceroute(self, target='8.8.8.8') -> str:
    functions.error_trapping([target, '** do_traceroute'])
    list_hops, return_result = icmplib_function.icmplib_traceroute(target)
    for variable_l in list_hops:
        self.hops.append(variable_l)
    return return_result


def split_string(temp) -> json:
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


def do_scapy_traceroute(target='8.8.8.8') -> list:
    trace_object = trace_class.HandleTraceroute
    output_list = scapy_function.scapy_traceroute(target)
    #
    # Need to place return into object and return the object.
    #
    return output_list


def set_external_ip_address(input_value: str) -> None:
    try:
        host_machine.set_host_environment_variables(input_value)
    except Exception as err:
        print('Error: {}'.format(err))


def get_external_ip_address(self) -> str:
    self.external_address = host_machine.get_host_external_ip_address()
    return self.external_address
