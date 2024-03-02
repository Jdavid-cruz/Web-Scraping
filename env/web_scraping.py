#---------------> WEB SCRAPING <----------------#
#Las bibliotecas que debemos utilizar para hacer Web Scraping son #beautifulsoup4, #lxml, #requests


# ¿COMO VER EL CÓDIGO FUENTE? #
import bs4
from bs4 import BeautifulSoup
import requests

resultado = requests.get("https://empresa.nestle.es/es") #--> De esta manera, sabemos a que Web vamos a analizar.

print(resultado.text) #--> Imprimimos el el codigo fuente de la web

sopa = bs4.BeautifulSoup(resultado.text, 'lxml') #-->Utilizamos lxml para hacer un parsing mas efectivo del documento HTML

print(sopa.select('p')[5].getText()) #-->De esta manera seleccionaos aquello que queremos analizar. Específicamos el índice, y luego eliminamos etiquetas y sólo veremos el texto que queremos ver.

parrafo_especial = sopa.select('p')[3].getText()
print(f"El parrafo especial es: ", parrafo_especial)

span_especial = sopa.select('div>span')[1].getText()
print(f"Mi span especial es: ", span_especial)


