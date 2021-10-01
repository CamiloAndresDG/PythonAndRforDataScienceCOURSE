#Tiddies
"""
Tibbles son un poco diferentes de los marcos de datos estándar. Un marco de 
datos es una colección de columnas, como una hoja de cálculo o una tabla SQL. 
Tibbles son como marcos de datos optimizados que se configuran automáticamente 
para extraer SOLO las primeras 10 filas de un conjunto de datos, y solo tantas 
columnas como puedan caber en la pantalla. 
"""

data(diamonds)

View(diamonds)

as_tibble(diamonds) #Muestra solo las 10 primeras filas

