"""
    Autor: Isaac Sánchez Verdiguel
    Materia: Web Security
    Grupo: 6CV2
"""

from scapy.all import *
import time
import os

# Obtiene la tabla ARP por medio de comandos
def get_arp_table():
    # Ejecutar el comando para obtener la tabla ARP
    result = os.popen("arp -a").read().strip()
    output = result.split('\n')
    return output

# Extrae la MAC del resultado del comando cuando la IP coincide
def extract_mac_from_arp(arp_table, router_ip):
    # Buscar la línea de la tabla ARP correspondiente al router
    for line in arp_table:
        auxiliar = line.split()[1]
        aux = str(auxiliar).replace('(', '').replace(')', '')
        if router_ip == aux:
            return line.split()[3]
    return None

# Obtiene la ip del router
def get_router_ip_mac():
    # Obtener la IP del router (gateway)
    result = os.popen("ip route | grep default").read().strip()
    router_ip = result.split()[2]
    router_mac = extract_mac_from_arp(get_arp_table(), router_ip)
    return router_ip, router_mac



def check_arp_spoofing(true_router_mac):
    router_ip, current_mac = get_router_ip_mac()
    
    if current_mac is None or router_ip is None:
        print("No se puede obtener la dirección MAC o la IP actual del router")
        return
    
    if current_mac.lower() == true_router_mac.lower():
        print("La tabla ARP no ha sido modificada. La dirección MAC del router es correcta.")
    else:
        print("¡Advertencia! La tabla ARP ha sido modificada. La dirección MAC del router es incorrecta.")
        print(f"IP del router: {router_ip}, MAC actual: {current_mac}, MAC esperada: {true_router_mac}")

if __name__ == "__main__":
    true_router_mac = input("Ingrese la dirección MAC verdadera del router: ")
    # Hace un loop eterno en el que analiza si hay modificaciones en el ARP
    while True:
        router_ip, current_mac = get_router_ip_mac()
        
        if current_mac is None or router_ip is None:
            print("No se puede obtener la dirección MAC o la IP actual del router")
        else:
            check_arp_spoofing(true_router_mac)
        time.sleep(2)
