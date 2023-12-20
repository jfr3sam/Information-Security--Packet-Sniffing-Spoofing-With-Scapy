from scapy.all import sniff

# Callback function to process each captured packet
def packet_callback(packet):
    print("Packet Summary:")
    print(packet.summary())
    
    # Further analysis for IP packets
    if packet.haslayer("IP"):
        print("Additional Information:")
        print(f"Source IP: {packet['IP'].src}")
        print(f"Destination IP: {packet['IP'].dst}")
    print("--------------")

# Sniff 10 packets and call packet_callback for each
sniff(count=10, prn=packet_callback)
