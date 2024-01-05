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


def split_string(temp) -> json:
    """
    This splits a string at a determined point, it assumes the items are in the correct place.
    This should be made flexible.
    :param temp:
    :return:
    """
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
    return temp_json

def search_for_first_external_hop(input_src: str, trace_object: trace_class.HandleTraceroute, check: bool):
    returning_variable = str(input_src)
    input_variable_test = str(input_src).split('.')[0]
    validation_variable = trace_object.get_external_address()
    if check == False:
        if input_variable_test in validation_variable:
            # this means it is an internal ip address
            return "", False  # this needs to be refined -> what to do
        else:
            # this means it is an external ip address
            print("search_for_first_external_hop() - {} - input_variable_test{} - check {}".format(returning_variable,
                                                                                        input_variable_test, check))
            return returning_variable, True
    else:
        return "", True


def temp_function(temp_object: trace_class.HandleTraceroute):
    print("This is the test - {}".format(temp_object.pop_hops()))

def adding_scapy_hop_returns_to_an_object(input_list: list, t_object: trace_class.HandleTraceroute) -> trace_class.HandleTraceroute:
    """
    Getting data out of the input list (list of hops json items), placing into a Hop object and return object.
    :param input_list: list
    :param t_object: trace_class.HandleTraceroute
    :return: t_object as yet unused
    """
    stop_repeating_check = False
    for o in input_list:
        # print("This is o of output_list: {} - {} - {}".format(o, o['dst'], o['src']))
        a = (t_object.Hop())
        a.add_dst(o['dst'])
        a.add_hop_id(o['id'])
        a.add_protocol(o['protocol'])
        a.add_ip_version(o['version'])
        a.add_src(o['src'])
        a.add_ttl(o['ttl'])
        functions.error_trapping(['appending_hops', a, ' - ', t_object.Hop().show_all()])
        external_ip_find, stop_repeating_check = search_for_first_external_hop(a.src, t_object, stop_repeating_check)
        t_object.append_hops(a)

    if not external_ip_find:
        # set this variable as external ip on host environment - if changed.
        host_object = host_machine
        host_object.set_host_environment_variables(external_ip_find)
    else:
        print("There was an issue finding the external ip address.")
    #
    # Need to place return into object and return the object.
    #
    # print("This will replace output_list: {} - {}".format('trace_object', trace_object.temp_hops.show_all()))
    return t_object


def do_scapy_traceroute(target='8.8.8.8') -> list:
    trace_object = trace_class.HandleTraceroute()
    output_list = scapy_function.scapy_traceroute(target)
    trace_object = adding_scapy_hop_returns_to_an_object(output_list, trace_object)
    print(" ** Okay ** {}".format(trace_object.temp_hops.show_all()))
    return output_list


def set_external_ip_address(input_value: str) -> None:
    try:
        host_machine.set_host_environment_variables(input_value)
    except Exception as err:
        print('Error: {}'.format(err))


def get_external_ip_address(self) -> str:
    self.external_address = host_machine.get_host_external_ip_address()
    return self.external_address

def do_icmplib_traceroute(self, target='8.8.8.8') -> str:
    """
    This is an alternate to scrapy traceroute library, as yet not functional.
    :param self:
    :param target:
    :return:
    """
    functions.error_trapping([target, '** do_traceroute'])
    list_hops, return_result = icmplib_function.icmplib_traceroute(target)
    for variable_l in list_hops:
        self.hops.append(variable_l)
    return return_result