#Organizar datos
#Sin los datos limpiados no se puede generar conocimiento
library(tidyverse)
library("palmerpenguins") #Importo los datos 
library("dplyr") #Importo la libreria para los pype

#ARRANGE
#Se organiza
penguins %>% arrange(bill_length_mm) #COn arrange se organizan los datos dependiendo de
 #La columna seleccionada, en este caso, organizara de menor a mayor por coluna bill_length_mm

penguins %>% arrange(-bill_length_mm) #en este caso, organizara de mayor a menor por coluna bill_length_mm

penguins2<-penguins %>% arrange(-bill_length_mm) #Almaceno el resultado en un nuevo Data Frame
View(penguins2)

#GROUP BY
#Se organiza dependiendo de columnas
penguins %>% group_by(island) %>%  drop_na %>%  summarise(mean_bill_length_mm= mean(bill_length_mm))
 #En este caso agrupe los datos por islas (me devolvera islas)
 #despues se hizo el drop_na apra eliminar los datos de la funte (hay que tener cuidado)
 #Por ultimo se hizo una media de los pinguinos con respecto a su bill_length_mm
 #El resultado sera una tabla con las islas y la media de los pinguinos en cada una

penguins %>% group_by(island) %>% drop_na() %>%  summarise(max)_bill_length_mm=max(bill_length_mm))
 #En este caso obtengo el maximo valor de bill_length_mm por isla

penguins %>% group_by(species,island) %>% drop_na() %>%  summarise(max)_bill_length_mm=max(bill_length_mm))
 #En este caso obtengo el maximo valor de bill_length_mm por especie y por isla

#FILTER
#Se filtran los datos
penguins %>%  filter(species=="Adelie") #Me trae el data frame con
 #solo los datos donde la especie del piguino sea Adelie
