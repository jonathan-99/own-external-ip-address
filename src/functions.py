try:
    import src.traceroute_class as trace
    import sys
    import json
except ImportError as e:
    sys.exit("Importing error: " + str(e))


def do_trace() -> None:
    """
    This does one traceroute and updates the machine's environmental variable.
    :return:
    """
    a = trace.HandleTraceroute()
    a.do_traceroute()
    a.check_hops_for_external_ip()
    a.get_external_ip_address()

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