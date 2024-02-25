
test_1 = """Begin emission: 
Finished sending 30 packets.
 .....*...............................
 Received 37 packets, got 1 answers, remaining 29 packets
   1.1.1.1:udp53
 1 10.7.5.2        11
 result QueryAnswer(query=<IP  id=33150 frag=0 ttl=1 proto=udp dst=1.1.1.1 | <UDP  sport=54475 |>>, 
 answer=<IP  version=4 ihl=5 tos=0x0 len=56 id=49683 flags= frag=0 ttl=64 proto=icmp chksum=0x9a5f src=10.7.5.2 dst=10.7.5.67 | 
 <ICMP  type=time-exceeded code=ttl-zero-during-transit chksum=0x665 reserved=0 length=0 unused=0 |
         <IPerror  version=4 ihl=5 tos=0x0 len=28 id=33150 flags= frag=0 ttl=1 proto=udp chksum=0x2708 src=10.7.5.67 dst=1.1.1.1 | 
         <UDPerror  sport=54475 dport=domain len=8 chksum=0x1992 |>>>>)"""

test_2 = """
Begin emission:
Finished sending 30 packets.
....*.*........*.*.*....................
Received 40 packets, got 5 answers, remaining 25 packets
 1.1.1.1:udp53      
1 192.168.1.1     11 
2 192.168.0.1     11 
4 2.120.8.75      11 
5 2.120.15.49     11 
6 172.71.176.4    11
  QueryAnswer(query=<IP  id=60817 frag=0 ttl=1 proto=udp dst=1.1.1.1 |
  <UDP  sport=644 |>>, answer=<IP  version=4 ihl=5 tos=0xc0 len=56 id=38668 flags= frag=0 ttl=64 proto=icmp chksum=0x5f40 src=192.168.1.1 dst=192.168.1.103 |
  <ICMP  type=time-exceeded code=ttl-zero-during-transit chksum=0xb92a reserved=0 length=0 unused=0 |
  <IPerror  version=4 ihl=5 tos=0x0 len=28 id=60817 flags= frag=0 ttl=1 proto=udp chksum=0x82f src=192.168.1.103 dst=1.1.1.1 |
  <UDPerror  sport=644 dport=domain len=8 chksum=0x3914 |>>>>)

"""

