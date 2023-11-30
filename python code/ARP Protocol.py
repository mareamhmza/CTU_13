from scapy.all import *

# ARP packet information
arp_packet = Ether(src="54:52:00:00:00:01", dst="ff:ff:ff:ff:ff:ff") / ARP(
    pdst="147.32.84.165", psrc="147.32.84.85"
)

# Sending ARP packet
sendp(arp_packet)
