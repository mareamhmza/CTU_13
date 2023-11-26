## summarize the information for each protocol:

### ARP (Address Resolution Protocol)
- **Packet Number (6):** ARP request sequence number.
- **Timestamp (52.369688):** Time of packet capture.
- **Source MAC (54:52:00:00:00:01):** MAC address of the requester.
- **Destination MAC (Broadcast):** Broadcast address for ARP request.
- **Ethernet Frame Type (ARP):** Indicates an ARP frame.
- **Frame Length (60):** Length of the Ethernet frame.
- **ARP Request Message:** Asking for the MAC address of 147.32.84.165 from 147.32.84.85.

### NBNS (NetBIOS Name Service)
- **Packet Number (15):** NBNS message sequence number.
- **Timestamp (162.765245):** Time of packet capture.
- **Source IP (147.32.84.165):** IP address of the NBNS message sender.
- **Destination IP (147.32.84.255):** Broadcast address for NBNS message.
- **Protocol (NBNS):** NetBIOS Name Service.
- **Frame Length (110):** Length of the Ethernet frame.
- **NBNS Message:** Registration request for the NetBIOS name "SARUMAN<00>."

### DNS (Domain Name System)
- **Packet Number (22):** DNS query sequence number.
- **Timestamp (163.929961):** Time of packet capture.
- **Source IP (147.32.84.165):** IP address of the DNS query sender.
- **Destination IP (147.32.80.9):** IP address of the DNS server.
- **Protocol (DNS):** Domain Name System.
- **Frame Length (64):** Length of the Ethernet frame.
- **DNS Query:** Standard query for the domain name "wpad."

### TCP (Transmission Control Protocol) - SYN
- **Packet Number (41):** TCP connection initiation sequence number.
- **Timestamp (166.207308):** Time of packet capture.
- **Source IP (147.32.84.165):** IP address of the connection initiator.
- **Destination IP (74.125.232.195):** IP address of the destination server.
- **Protocol (TCP):** Transmission Control Protocol.
- **Frame Length (62):** Length of the Ethernet frame.
- **TCP Flags:** Out-Of-Order, Port numbers reused.
- **TCP Details:** SYN packet for connection initiation.

### TCP - RST (Reset) and ACK (Acknowledgment)
- **Packet Number (49):** TCP connection termination with RST and ACK sequence number.
- **Timestamp (166.252423):** Time of packet capture.
- **Source IP (147.32.84.165):** IP address of the device terminating the connection.
- **Destination IP (74.125.232.195):** IP address of the server.
- **Protocol (TCP):** Transmission Control Protocol.
- **Frame Length (60):** Length of the Ethernet frame.
- **TCP Details:** RST and ACK flags, indicating termination with acknowledgment.

### IGMPv3 (Internet Group Management Protocol version 3)
- **Packet Number (71):** IGMPv3 message sequence number.
- **Timestamp (173.094785):** Time of packet capture.
- **Source IP (147.32.84.165):** IP address of the device sending the IGMPv3 message.
- **Destination IP (224.0.0.22):** Multicast group address.
- **Protocol (IGMPv3):** Internet Group Management Protocol version 3.
- **Frame Length (60):** Length of the Ethernet frame.
- **IGMPv3 Message:** Membership report, joining group 239.255.255.250 for any sources.

### SSDP (Simple Service Discovery Protocol)
- **Packet Number (83):** SSDP message sequence number.
- **Timestamp (181.288332):** Time of packet capture.
- **Source IP (147.32.84.165):** IP address of the device sending the SSDP message.
- **Destination IP (239.255.255.250):** Multicast group address.
- **Protocol (SSDP):** Simple Service Discovery Protocol.
- **Frame Length (175):** Length of the Ethernet frame.
- **SSDP Message:** M-SEARCH (multicast search) request for devices or services.

### HTTP
- **Packet Number (171):** HTTP request sequence number.
- **Timestamp (298.231859):** Time of packet capture.
- **Source IP (147.32.84.165):** IP address of the device sending the HTTP request.
- **Destination IP (60.190.223.75):** IP address of the server.
- **Protocol (HTTP):** Hypertext Transfer Protocol.
- **Frame Length (155):** Length of the Ethernet frame.
- **HTTP Request:** GET request for the resource "/p/out/kp.exe" using HTTP version 1.0.

