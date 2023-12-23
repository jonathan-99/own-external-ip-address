try:
    from icmplib import traceroute
    import sys
    import json
    import os
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

    def check_ip_address_if_external(self, input_var) -> bool:
        if input_var in self.internal_address:
            return False
        else:
            return True


    def set_external_ip_address_to_env_var(self) -> None:
        pass
        # output = self.external_address

    def do_traceroute(self, target='8.8.8.8') -> None:
        # execute
        hop = traceroute(target)
        last_distance = 0
        for h in hop:
            if last_distance + 1 != h.distance:
                print('gateways ae not responding')
        # save hop to internal values
            self.hops.append(h.address)
        # loop
            last_distance = h.distance

    def print_hops(self) -> None:
        for h in self.hops:
            print(h)

    def get_hops(self) -> json:
        output = ''
        for h in self.hops:
            output += h
        return {'hops': output}

    def test_loop_return(self) -> json:
        return {'test': str([h for h in self.hops])}

    def set_external_ip_address(self, input) -> None:
        self. external_address = input



    def check_hops_for_external_ip(self) -> str:
        pass

    def get_external_ip_address(self) -> str:
        return self.external_address



    def show_details(self) -> None:
        print('This is...{}'.format(self.internal_address))