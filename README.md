
# Tarea Final: Spoofing w/ Python WBS 

El objetivo es desarrollar dos códigos en Python: un código que permita atacar con spoofing a una máquina virtual (víctima) cambiando la MAC del router por la MAC de la máquina virtual (atacante) y un código que permita detectar cuando este ataque fue realizado.

Lo anterior es ejecutado en un entorno seguro con una máquina virtual de Kali Linux y un servidor de Ubuntu conectados a un mismo router dentro de VirtualBox.






## Authors

- Isaac Sánchez Verdiguel [@iscko5](https://github.com/iscko5)
- Grupo: 6CV2 Web Security


## Instalación

Se necesitan los siguientes requerimientos para ejecutar la práctica:
- Una máquina virtual de Kali Linux con al menos 2 GB de memoria RAM virtual.
- Una máquina virtual de cualquier sistema operativo con al menos 2 GB de memoria RAM virtual.
- Python3.
- Librerías de Python: *Scapy*, *time* y *os* (vease instalación debajo)
- Conocimiento en comandos de configuración de red.

### Modificación de las máquinas virtuales
Para poder comunicar las máquinas virtuales en una sola network, se configuró cada equipo de la siguiente manera:

1. Se instala la máquina virtual
2. En la configuración de red, se habilita la opción **"Adaptador Puente"**
3. Se repite el paso para la siguiente máquina virtual

Esto proporciona una IP Address a cada máquina virtual y permite la conexión por medio del router [1]. Con fines prácticos, cada máquina tiene una MAC única (será la que se reemplaze en la práctica) y una conexión al mismo router del host.


#### Instalación de Python y sus librerías

Los siguientes comandos fueron ejecutados en ambas máquinas virtuales para actualizar Python a su versión más reciente

```bash
  sudo apt install python3-pip -y
  pip install scapy

```
    
## Pasos Previos a Ejecución

Para ejecutar el proyecto, se debe primero conocer las siguientes variables:

#### Máquina Víctima

- Dirección IP del router
- Dirección MAC del router
- Dirección IP de la máquina virtual

Para obtener la dirección IP del router se emplea el siguiente comando:
```bash
  ip route | grep default
```

Para obtener la dirección MAC del router se emplea el siguiente comando en el cuál se busca la dirección IP del comando anterior:
```bash
  arp -a
```
Para obtener la dirección IP de la máquina virtual se emplea el siguiente comando:
```bash
  ip a
```

#### Máquina Atacante

- Dirección MAC propia

Para obtener la dirección MAC del router se emplea el siguiente comando en el cuál se busca la dirección IP de la máquina virtual:
```bash
  arp -a
```




## Ejecución del Proyecto

Para ejecutar el proyecto se recomienda seguir estos pasos:

### Ejecutar el Detector de Spoofing
Ejecutar el código que detecta algún ataque de tipo spoofing en la máquina virtual de la víctima con el siguiente comando:

```bash
  sudo python3 detect_spoofing.py
```

El código entrará en un loop dónde cada dos segundos se dará el estatus más actual de la tabla ARP para identificar si la MAC original ha sido cambiada, detectando así un ataque.

Se recomienda ejecutar primero este código para tener el control desde antes de modificar la MAC de las acciones que suceden.

### Ejecutar Ataque Spoofing

Ejecutar el código que ataca a la víctima conociendo el IP del router y del equipo de la víctima. Esto ocasionará que se pueda empaquetar el ataque para reemplazar la MAC del destino. Se ejecuta con el siguiente comando:

```bash
  sudo python3 spoofing.py
```
El programa solicitará la IP del router y de la máquina virtual, con esta información será capaz de detectar la MAC que atacará. El paquete será enviado a la víctima y no parará hasta tener alguna interrupción por teclado.




## Referencias

[Virtual Box Networks](https://forums.virtualbox.org/viewtopic.php?t=96608)

[Spoofer Guide](https://www.geeksforgeeks.org/python-how-to-create-an-arp-spoofer-using-scapy/)

[Comandos de ARP](https://www.geeksforgeeks.org/arp-command-in-linux-with-examples/)


