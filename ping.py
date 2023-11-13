import socket

url = input('Ingrese URL del sitio deseado: ')

try:
    ip = socket.gethostbyname(url)
    print(f"La dirección IP del sitio es: {ip}")
except socket.gaierror:
    print(f"No se pudo obtener la dirección IP del sitio")