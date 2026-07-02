from scapy.all import sniff
def packet_Callback(packet):
    print("Packet Reiceved")
sniff(prn=packet_Callback, count=10)

