from scapy.all import *

# TCP RST, ACK packet information
tcp_rst_ack_packet = IP(src="147.32.84.165", dst="74.125.232.195") / TCP(
    sport=1027, dport=80, flags="RA", seq=394, ack=78, window=0
)

# Sending TCP RST, ACK packet
send(tcp_rst_ack_packet)
