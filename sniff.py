from scapy.all import sniff, IP, UDP, TCP, ICMP, Raw

def packet_Callback(packet):
    print("==========================================================")
    print("Packet Received")

    if packet.haslayer(IP):
        print()
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

    if packet.haslayer(TCP):
        print()
        print("Protocol: TCP")

    elif packet.haslayer(UDP):
        print()
        print("Protocol: UDP")

    elif packet.haslayer(ICMP):
        print()
        print("Protocol: ICMP")

    if packet.haslayer(Raw):
        print()
        print("Raw Data:", packet[Raw].load)
    else:
        print()
        print("Raw Data: No Payload")


sniff(prn=packet_Callback, count=3)