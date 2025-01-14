###Pipe
#Es una herramienta para expresar una secuencia de multiples operaciones, representado con "%>%"
#Ayuda al codigo ser mas eficiente y facil pra leer y entender

##Nested
#En programacion describe el c�digo que realiza una funci�n particular y est� 
#contenido dentro del c�digo que realiza una funci�n m�s amplia. 
data("ToothGrowth") #Para cargar un data set que esta ya se usa la funcion data
View(ToothGrowth) #Para checar

install.packages("dplyr")
library(dplyr)

filtered_tg<-filter(ToothGrowth,dose==0.5) #Mostrara los datos en donde dose sea igual a 0.5
View(filtered_tg)

arrange(filtered_tg,len) #Para ordenar de menor a mayor, en este caso, por len

#Ahora con nested
arrange(filter(ToothGrowth,dose==0.5),len) #Mismo resultado que arriva

#Ahora con Pipe (Para sacar el pipe ctrl+shift+m)
filtered_toothgrowth<-ToothGrowth %>% #Se asigna a una nueva variable y se pone el dataset
  filter(dose==0.5) %>% #Se hace el primer filtro de dose==0.5
  arrange(len) #Se hace la organizacion de mayor a menor

View(filtered_toothgrowth)#Se muestra

#Otro ejemplo
#Ahora con Pipe (Para sacar el pipe ctrl+shift+m)
filtered_toothgrowth2<-ToothGrowth %>% #Se asigna a una nueva variable y se pone el dataset
  filter(dose==0.5) %>% #Se hace el primer filtro de dose==0.5
  group_by(supp) %>% 
  summarise(mean_len=mean(len,na.rm=T),.group="drop") #Se le dice a R qu� hacer 
  #con los valores faltantes y para asegurarse de que los datos est�n agrupados de la manera correcta cuando agregamos la funci�n de resumen. 
View(filtered_toothgrowth2)

#Para recordar
#Siempre se tiene que poner donde sea necesario el %>% 
#Se tiene que identar