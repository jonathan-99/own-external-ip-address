try:
    import src.functions as functions
    import sys
    import json
    import os
except ImportError as e:
    sys.exit("Importing error: " + str(e))

ext_ip_address = 'EXT_IP_ADDRESS'

def set_host_environment_variables(address: str) -> None:
    functions.error_trapping(['setting host machine()', ext_ip_address, type(address), address])
    try:
        if not os.environ[ext_ip_address]:
            if os.environ[ext_ip_address] != address:
                # this means the external address is different to that set
                os.environ[ext_ip_address] = address
            else:
                # this means the external address is the same -> no change
                pass
        else:
            # this means the environmental variable is empty -> so set it
            os.environ[ext_ip_address] = address
    except OSError as err:
        print('Error: {}. invalid, inaccessible like names or paths, or other arguments that have the correct type, '
              'but are not accepted by the OS'.format(str(err)))

def get_host_external_ip_address() -> str:
    return os.environ[ext_ip_address]
