try:
    import testing.traceroute_class as trace
    import sys
    import json
    import host_machine_class
except ImportError as e:
    sys.exit("Importing error: " + str(e))


def do_trace() -> None:
    """
    This does one traceroute and updates the machine's environmental variable.
    :return:
    """
    a = trace.HandleTraceroute()
    a.do_traceroute()
    ext_address = a.check_hops_for_external_ip_and_return()
    print("This should be an external IP address".format(ext_address))
    host_machine_class.set_host_environment_variables(ext_address)

def check_for_change() -> None:
    """
    This compares the machine's environmental variable for change.
    :return:
    """
    a = trace.HandleTraceroute()
    a.do_traceroute()
    a.check_hops_for_external_ip()
    a.get_external_ip_address()
    a.get_existing_external_ip_address()


if __name__ == '__main__':
    check_for_change()