from scapy.all import *

# HTTP packet information
http_packet = IP(src="147.32.84.165", dst="60.190.223.75") / TCP(
    sport=49152, dport=80, flags="PA", seq=1, ack=1
) / "GET /p/out/kp.exe HTTP/1.0\r\n\r\n"

# Sending HTTP packet
send(http_packet)
