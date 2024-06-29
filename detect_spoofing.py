from scapy.all import *
import os

def get_mac(ip):
    try:
        return getmacbyip(ip)
    except:
        return None

def check_arp_spoofing(router_ip, true_router_mac):
    current_mac = get_mac(router_ip)
    
    if current_mac is None:
        print("No se puede obtener la dirección MAC actual del router")
        return
    
    if current_mac.lower() == true_router_mac.lower():
        print("La tabla ARP no ha sido modificada. La dirección MAC del router es correcta.")
    else:
        print("¡Advertencia! La tabla ARP ha sido modificada. La dirección MAC del router es incorrecta.")
        print(f"MAC actual: {current_mac}, MAC esperada: {true_router_mac}")

if __name__ == "__main__":
    router_ip = input("Ingrese la IP del router: ")
    true_router_mac = input("Ingrese la dirección MAC verdadera del router: ")
    check_arp_spoofing(router_ip, true_router_mac)
