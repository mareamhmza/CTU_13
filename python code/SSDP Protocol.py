from scapy.all import *

# SSDP packet information
ssdp_packet = IP(src="147.32.84.165", dst="239.255.255.250") / UDP(dport=1900) / Raw(
    load="M-SEARCH * HTTP/1.1"
)

# Sending SSDP packet
send(ssdp_packet)
