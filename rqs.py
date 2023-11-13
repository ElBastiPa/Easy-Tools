import requests

ip_address = '81.88.53.67'

api_key = '339b7b529162f8'

url = f'https://ipinfo.io/{ip_address}/json?token={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Información de la dirección IP:")
    print(f"IP: {data['ip']}")
    print(f"Ubicación: {data['city']}, {data['region']}, {data['country']}")
    print(f"Proveedor de Internet: {data['org']}")
else:
    print("Error al obtener información de la dirección IP.")
