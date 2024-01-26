from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1
import time
import socket

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

def run_traceroute(dest, max_hops=30):
    for ttl in range(1, max_hops + 1):
        own_address = get_host_ip()
        packet = IP(src=own_address, dst=dest, ttl=ttl) / ICMP()  # src="192.168.1.103"
        print(f"Sending ICMP packet for Hop {ttl}")
        response = sr1(packet, timeout=1, verbose=1)

        if response:
            print(f"Received response for Hop {ttl}")
            hop_info = get_hop_info(response)
            if hop_info:
                print(f"Hop {ttl} Information:", hop_info)

                # Check if the source IP matches the input destination IP
                if hop_info['src'] == dest:
                    print("Reached the destination. Stopping traceroute.")
                    break
            else:
                print(f"No IP layer found for Hop {ttl}.")
        else:
            print(f"No response for Hop {ttl}.")

        time.sleep(1)  # Add a delay between hops

if __name__ == '__main__':
    run_traceroute("8.8.8.8")
