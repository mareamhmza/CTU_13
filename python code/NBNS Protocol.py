from scapy.all import *

# NBNS packet information
nbns_packet = IP(src="147.32.84.165", dst="147.32.84.255") / UDP(dport=137) / NBNS(
    query="Registration NB SARUMAN<00>"
)

# Sending NBNS packet
send(nbns_packet)
