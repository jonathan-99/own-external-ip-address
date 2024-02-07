#!/usr/bin/env python3

try:
    import logging
    import src.icmplib_traceroute as icmplib_function
    import src.scapy_traceroute as scapy_function
    import src.new_scrapy_traceroute as new_scapy_function
    import src.functions as functions
    import src.traceroute_class as trace_class
    import sys
    import json
    import os
    import src.host_machine_class as host_machine
except ImportError as e:
    import logging
    logging.error("Importing error: (scapy_traceroute.py)" + str(e))
    sys.exit()
except Exception as err:
    import logging
    logging.error(f"This is a wider error catch - {err}")



def do_scapy_traceroute(target='8.8.8.8'):
    # do a trace and gather all data
    trace_object = trace_class.HandleTraceroute()
    new_scapy_function.run_traceroute(target, trace_object)

    # select through for the first external ip address.
    external_ip_address = trace_object.return_first_external_hop()
    print(f" ** Okay ** {external_ip_address}")
    host_machine.set_host_environment_variables(external_ip_address)



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


if __name__ == '__main__':
    print("We are here: ".format(do_scapy_traceroute(target='8.8.8.8')))
