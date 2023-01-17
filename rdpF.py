import subprocess
from concurrent.futures import ThreadPoolExecutor

# Obtener la dirección IP local
ip = socket.gethostbyname(socket.gethostname())

# Obtener la mascara de subred
subnet = ip.rsplit(".", 1)[0] + "."

# Lista para almacenar los resultados
results = []

def check_host(host):
    hostname = subnet + str(host)
    try:
        # Realizar ping al host
        subprocess.check_output("ping -c 4 " + hostname, shell=True, stderr=subprocess.DEVNULL)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect((hostname, 3389))
            print(hostname + " tiene el puerto 3389 abierto.")
            s.shutdown(2)
        except:
            pass
    except subprocess.CalledProcessError as error:
        pass

# Ejecutar escaneo en paralelo
with ThreadPoolExecutor() as executor:
    for host in range(1, 51):
        executor.submit(check_host, host)
    for host in range(100, 150):
        executor.submit(check_host, host)
