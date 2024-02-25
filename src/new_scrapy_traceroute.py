#!/usr/bin/env python3

try:
    import logging
    from scapy.layers.inet import IP, ICMP
    from scapy.sendrecv import sr1
    import time
    import socket
    import src.traceroute_class as trace_class
    import sys
except ImportError as e:
    import logging
    logging.error("Importing error: (scapy_traceroute.py)" + str(e))
    sys.exit()
except Exception as err:
    import logging
    logging.error(f"This is a wider error catch - {err}")


def get_host_ip():
    try:
        # Use a socket to get the host name and IP address
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip
    except socket.error as e:
        print(f"Error: {e}")
        return None


def get_hop_info(packet):
    try:
        ip_layer = packet[IP]
        hop_info = {
            'src': ip_layer.src,
            'dst': ip_layer.dst,
            'ttl': ip_layer.ttl,
            'proto': ip_layer.proto
            # Add more fields as needed
        }
        return hop_info
    except IndexError:
        # Handle the case when IP layer is not present
        return None


def run_traceroute(destination, trace_object: trace_class.HandleTraceroute, max_hops=30):
    for ttl in range(1, max_hops + 1):
        own_address = get_host_ip()
        packet = IP(src=own_address, dst=destination, ttl=ttl) / ICMP()  # src="192.168.1.103"
        response = sr1(packet, timeout=1, verbose=1)

        if response:
            hop_info = get_hop_info(response)
            if hop_info:
                trace_object.append_hops(ttl, hop_info)
                logging.debug(f'Hop {ttl} Information: {hop_info}')
                print(f'Hop {ttl} Information: {hop_info}')

                # Check if the source IP matches the input destination IP
                if hop_info['src'] == destination:
                    print("Reached the destination. Stopping traceroute.")
                    break
            else:
                error_return = f'No IP layer found for hop {ttl}'
                logging.error(error_return)
        else:
            error_return = f"No response for Hop {ttl}."
            logging.error(error_return)

        time.sleep(1)  # Add a delay between hops


if __name__ == '__main__':
    trace_object_upper = trace_class.HandleTraceroute()
    run_traceroute("8.8.8.8", trace_object_upper)
    print(f'running new_scrapy_traceroute.py - {trace_object_upper.show_details()}')
