#!/usr/bin/env python3

try:
    import src.icmplib_traceroute as icmplib_function
    import src.scapy_traceroute as scapy_function
    import src.functions as functions
    import sys
    import json
    import os
    import src.host_machine_class
except ImportError as e:
    sys.exit("Importing error: " + str(e))


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

    def do_scapy_traceroute(self, target='8.8.8.8') -> str:
        output, errors = scapy_function.scapy_traceroute(target)
        if not errors:
            functions.error_trapping([output, errors])
            return output
        else:
            functions.error_trapping([output, errors])
            print("Errors with scapy traceroute - {}".format(errors))
            return output

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
            host_machine_class.set_host_environment_variables(input_value)
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
        self.external_address = host_machine_class.get_host_external_ip_address()
        return self.external_address

    def show_details(self) -> None:
        everything = str(self.internal_address) + \
            str(self.external_address) + \
            str(self.hops) + \
            self.a_pipper
        print('This is everything...{}'.format(everything))