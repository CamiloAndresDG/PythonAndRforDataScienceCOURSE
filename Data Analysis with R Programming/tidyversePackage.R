#tidyverse
###Los paquetes mas usados
#ggplot
#Sirve para mostrar una gran variedad de visializacion de los datos aplicando diferentes propiedades
#a las variables de los datos en R
install.packages('palmerpenguins')
library('palmerpenguins')

install.packages('ggplot2')
library('ggplot2')

ggplot(data=penguins,aes(x=flipper_length_mm, y=body_mass_g))+geom_point(aes(shape=species,color=species))+facet_wrap(~species)

#tidyr 
#Es un paquete para la limpieza de los datos para hacer datos ordenados

#readr
#Es un paquete usado para importar los datos

#dplyr
##Es un paquete con un conjunto de funciones basicas necesarias para la manipulacion de los datos para completar 
#una tarea

##Los otros paquetes
#tibble
#Trabaja con marcos de datos

#purrr
#Trabaja con funciones y vectores haciendo que el codigo sea mas facil de escribir y entender

#stringr
#Tiene funciones que hacen mas facil trabajar con Strings

#forcats
#Provee herramientas que resuelven prblemas comunes con factores
 #Factors o factores: Almacena datos categorios dnde los valores de los datos son limitados y usualmente basados en 
#un grupo finitio de datos 
