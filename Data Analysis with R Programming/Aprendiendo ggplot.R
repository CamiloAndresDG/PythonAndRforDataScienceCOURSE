install.packages("tydiverse") #Instalar el paquete
library("ggplot2") #Se trae la libreria de ggplot2
library("palmerpenguins") #Se traen los datos con los que se va a trabajar

ggplot(data=penguins)+geom_point(mapping=aes(x=flipper_length_mm,y=body_mass_g)) #Muestra la relacion entre body_mass y flipper_length
  #ggplot()=se agrega con que datos vamos a trabajar
  #LAYERS
  #geom=es un objeto geometrico usado para representar los datos
  #geom_point=le dice a R que se cree en en puntos y crear un grafico de dispersion
  #Aesthetic=una propiedad visual de un objeto en el plot
  #aes=Define el mapping entre los datos y el plot

#PASOS PARA HACER PLOT CON GGPLOT
#Comenzar el ggplot funcion y escoger un dataset para trabajar
#Agregar el geom_funcion para mostrar los datos
#Mapear las variables que se quieren en el plot en los argumentos de la funcion aes()

#ggplot(data=<DATA>)+<GEOM_FUNCTION>(mapping=aes(<AESTHETIC MAPPINGS>))

ggplot(data=penguins)+geom_point(mapping=aes(x=bill_length_mm,y=bill_depth_mm)) #Muestra la relacion entre bill_length_mm y bill_depth_mm

#De esta manera se puede obtener documentacion
?geom_point
