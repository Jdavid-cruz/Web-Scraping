#----¿CÓMO EXTRAER ELEMENTOS DE UNA CLASE?----#

"""
Carácter                        SINTAXIS                        RESULTADOS
    "                       soup.select('div')                     Todos los elementos con la etiqueta div
    #                       soup.select('#estilo_4')               Todos los elementos que contengan id ='estilo4'
    .                       soup.select('.columna_der')            Elementos que contengan class ='columna_der'
    (ESPACIO)               soup.select('div span')                Cualquier elemento llamado span dentro de un elemento div
    >                       soup.select('div>span')                 Cualquier elemento llamado span directamente dentro de un elemtno div sin nada en el medio.

"""