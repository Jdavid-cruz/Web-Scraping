import bs4
from bs4 import BeautifulSoup
import requests

url_base = 'http://books.toscrape.com/catalogue/page-{}.html' #--> gracias a: {}, podemos movernos por las páginas que queramos

# lista de título con 4 o 5 estrellas 

titulos_rating_alto = []

#iterar páginas 
for pagina in range(1,51):
    #crear sopa en cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    #iterar libros
    for libro in libros: 
        #comprobar que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):

            #guardar título en variable
            titulo_libro = libro.select('a')[1]['title']

            #Agregar el libro a la lista
            titulos_rating_alto.append(titulo_libro)
    
# ver libros de 4 u 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)