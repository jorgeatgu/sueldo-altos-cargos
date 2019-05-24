
from bs4 import BeautifulSoup
import requests
import html5lib
import csv

url = 'https://sueldode.org/alto-cargo-ccaa/'

headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)

data = response.text

soup = BeautifulSoup(data, 'html5lib')

contenedor_lista = soup.find('div', {"class": "entry-content"})

lista_sueldos = contenedor_lista.findNext('ul')

# Buscamos todos los enlaces
links_sueldos = lista_sueldos.find_all('a')


# Ahora vamos a guardar todo en un CSV, lo primero es abrir el fichero.
# La sentencia with se encargará de cerrar el fichero como es debido cuando termine con él, si no habría que llamar a f.close()
with open('lista-enlaces.csv', 'w') as f:
    # Lo segundo es crear el escritor de CSV
    fileCSV = csv.writer(f)
    # Ahora añadimos las columnas del CSV
    fileCSV.writerow(['Nombre', 'Enlace'])

    for elem in links_sueldos:
        # Nos quedamos con el contenido del enlace
        nombre = elem.get('title')
        # Ahora nos quedamos con el enlace
        link = elem.get('href')
        # Ahora le pasamos todos los parametros al CSV que hemos creado anteriormente
        fileCSV.writerow([nombre, link])
