import os
import socket

# Obtener la dirección IP local
ip = socket.gethostbyname(socket.gethostname())

# Obtener la mascara de subred
subnet = ip.rsplit(".", 1)[0] + "."

for host in range(1, 255):
    # Crear la dirección IP completa
    hostname = subnet + str(host)

    # Realizar ping al host
    response = os.system("ping -c 1 " + hostname)

    if response == 0:
        print(hostname + " está encendido.")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect((hostname, 3389))
            print(hostname + " tiene el puerto 3389 abierto.")
            s.shutdown(2)
        except:
            print(hostname + " no tiene el puerto 3389 abierto.")
    else:
        print(hostname + " está apagado.")
