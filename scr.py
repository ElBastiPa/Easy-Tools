import requests
from bs4 import BeautifulSoup

url = 'https://cual-es-mi-ip.net/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    ip_element = soup.select_one('span')

    if ip_element:
        ip = ip_element.get_text()
        print("Tu dirección IP es:", ip)
    else:
        print("No se pudo encontrar la dirección IP en la página.")

else:
    print("Error al obtener la página. Código de estado:", response.status_code)
