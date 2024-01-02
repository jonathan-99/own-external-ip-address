#!/usr/bin/env python3
try:
    import src.trace_management as trace
    import src.traceroute_class as trace_class
    import sys
    import json
    import src.host_machine_class as host_machine_class
except ImportError as e:
    sys.exit("Importing error: " + str(e))


def error_trapping(value: list) -> None:
    for v in value:
        print("Error trapping: {}, {}".format(type(v), value))


def do_trace() -> None:
    """
    This does one traceroute and updates the machine's environmental variable.
    :return:
    """
    trace_class.HandleTraceroute()
    # error_trapping(['trace result in do_trace()', output_result])


def check_for_change() -> None:
    """
    This compares the machine's environmental variable for change.
    :return:
    """
    a = trace_class.HandleTraceroute()
    b = trace.do_scapy_traceroute()
    a.check_hops_for_external_ip()
    a.get_external_ip_address()
    a.get_existing_external_ip_address()


if __name__ == '__main__':
    check_for_change()
