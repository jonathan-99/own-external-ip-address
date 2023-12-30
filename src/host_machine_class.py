try:
    from icmplib import traceroute
    import sys
    import json
    import os
except ImportError as e:
    sys.exit("Importing error: " + str(e))

ext_ip_address = 'EXT_IP_ADDRESS'

def set_host_environment_variables(address) -> None:
    print("Here: {}".format(ext_ip_address, type(address), address))
    try:
        os.environ[ext_ip_address] = address
    except OSError as err:
        print('Error: {}. invalid, inaccessible like names or paths, or other arguments that have the correct type, '
              'but are not accepted by the OS'.format(str(err)))

def get_host_external_ip_address() -> str:
    return os.environ[ext_ip_address]
