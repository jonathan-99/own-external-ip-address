try:
    import src.functions as functions
    import sys
    import json
    import os
    import logging
except ImportError as e:
    sys.exit("Importing error: host_machine_class.py" + str(e))

ext_ip_address = 'EXT_IP_ADDRESS'


def set_host_environment_variables(address: str) -> None:
    # Assuming ext_ip_address is a variable containing the name of the environment variable
    functions.error_trapping(['setting host machine()', ext_ip_address, type(address), address])

    try:
        # Extract the string value from the dictionary
        address_str = json.dumps(address)  # Convert dictionary to JSON string
        if ext_ip_address in os.environ and os.environ[ext_ip_address]:
            # Check if the existing value is different from the new address
            if os.environ[ext_ip_address] != address:
                # Update the environment variable with the new address
                os.environ[ext_ip_address] = address
                print(f"Updated {ext_ip_address} environment variable with address: {address}")
            else:
                # Address is already set, no change needed
                print(f"{ext_ip_address} environment variable is already set to {address}, no change needed")
        else:
            # Set the environment variable with the new address
            os.environ[ext_ip_address] = address_str
            print(f"Set {ext_ip_address} environment variable with address: {address}")
    except KeyError:
        logging.debug('KeyError: The key {ext_ip_address} does not exist in the os.environ dictionary.')
    except OSError as err:
        logging.debug(f"Error: {err}. Unable to set environment variable.")


def get_host_external_ip_address() -> str:
    return os.environ[ext_ip_address]
