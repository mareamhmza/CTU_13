from scapy.all import *

# IGMPv3 packet information
igmpv3_packet = IP(src="147.32.84.165", dst="224.0.0.22") / IGMP(type=0x16, gaddr="239.255.255.250")

# Sending IGMPv3 packet
send(igmpv3_packet)
