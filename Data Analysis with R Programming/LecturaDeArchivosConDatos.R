install.packages("here"") #Hace la referencia a los archivos faciles
library("here"")

#Los sigueintes simplifica la tarea de limpieza de datos
install.packages("skimr")
library("skimr")

install.packages("janitor")
library("janitor")

#Ahora para verificar que tenemos dplyr
install.packages("dplyr")
library("dplyr")

#Si quiero cargar un archivo csv
 #read_csv()

install.packages("palmerpenguins")
library("palmerpenguins")

#Para poder hacer resumenes de los datos
 #skim_without_charts()
 #glimpse()
 #head()
 #select()

#EJEMPLO
skim_without_charts(penguins) #Nos da datos generales como el no. de columnas. rows, tipos de datos, etc.

glimpse(penguins) #Nos da n. filas y columnas

head(penguins) #Se obtiene una previa vista de los datos (los 6 primeros datos)

penguins %>% select(species) #Se extrajo la tabla species de penguins
penguins %>% select(-species) #Se extrageron todas las tablas menos species


#Para poder cambiar el nombre de una tabla
penguins %>% rename(island_new=island) #Cambio a island_new la tabla island

#Si se quiere hacer un cambio a todos los nombres de la tabla
rename_with(penguins,toupper)#Cambia todas las tablas a mayusculas
rename_with(penguins,lower)#Cambia todas las tablas a minusculas

#Para asegurar que las tablas son unicas y consistentes
clean_names(penguins)




