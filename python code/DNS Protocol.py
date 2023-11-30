from scapy.all import *

# DNS packet information
dns_packet = IP(src="147.32.84.165", dst="147.32.80.9") / UDP(dport=53) / DNS(
    rd=1, qd=DNSQR(qname="wpad", qtype="A")
)

# Sending DNS packet
send(dns_packet)
