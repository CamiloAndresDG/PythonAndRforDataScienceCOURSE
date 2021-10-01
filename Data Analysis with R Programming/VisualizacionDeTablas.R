#Limpiando y organizando datos

#DATA FRAMES
#QUe es un data frame?
 #Es una coleccion de columnas
#Se tienen que poner nombres a las columnas
#Puede almacenar diferentes tipos de datos

#TIBBLES
#No cambian los tipos de datos de entrada
#Nunca cambia los nombres de las variables
#La impresion es mas facil

install.packages("tidyverse") #Instalamos el paquete
library(ggplot2) #Se trae la libreria ggplot
data("diamonds") #Se toma el data set diamonds

View(diamonds) #Se muestra

head(diamonds) #Mostrara solo los 6 primeros datos del data set

str(diamonds) #Mostrara la estructura del data set
  #Sirve para entender que maneja cada columna

colnames(diamonds) #Mostrara unicamente el nombre de las columnas

library(tidyverse)

mutate(diamonds, carat_new=carat*100) #Con mutate podremos agregar nuevas columnas
  #En este caso agregue al dataset diamonds una nueva columna llamada
  #carat_new y esta contendra los datos de carat*100