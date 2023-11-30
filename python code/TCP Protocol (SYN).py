from scapy.all import *

# TCP SYN packet information
tcp_syn_packet = IP(src="147.32.84.165", dst="74.125.232.195") / TCP(
    sport=1027, dport=80, flags="S", seq=0, window=64240, options=[("MSS", 1460)]
)

# Sending TCP SYN packet
send(tcp_syn_packet)
