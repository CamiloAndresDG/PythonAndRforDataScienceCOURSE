print("Hola mundo")

## En programacion las estucturas de datos son un formato para organizar y almacenar datos

#Para obtener ayuda de la funcion print
?print()

#Las variables no pueden inciar en nombres!!

first_variable<-"This is my variable"
second_variable<-12.5

#Creacion de vectores
vec_1<-c(1,2,30,12,5.5)

#Pipe es una secuencia de multples operaciones (%>%) y es usado para usar el output de una funcion dentro de otra funcion

#CREACION DE VECTORES (Atomicos, solo pueden contener valores del mismo tipo)
x1<-c(22,2,2)
x2<-c(1L, 5L, 15L)
x3<-c("Sara","Antonio","Yukiko")
x4<-c(TRUE,FALSE,FALSE,FALSE,TRUE)

#Para saber que tipo de datos almacena el vector
typeof(c(22,2,2))
typeof(c(1L, 5L, 15L))
typeof(c("Sara","Antonio","Yukiko"))
typeof(c(TRUE,FALSE,FALSE,FALSE,TRUE))
#Tambien se puede comprobar si es de un tipo en especifico
is.double(x1)
is.character(x1)

#Para saber el tamanio del vector
length(x3)

#Para asignar un nombre a los datos de un vector
names(x1)<-c("Hola","Mundo") #Se agrega cada nombre respectivamente a la columna en la pos escrita
print(x1)
#EJEM 2
nombre <- c("Shrek", "Shrek 2", "Shrek Tercero", "Shrek: Felices por siempre")
puntuacion <- c(7.9, 7.2, 6.1, 6.3)
posterior_2005 <- c(FALSE, FALSE, TRUE, TRUE)

#CREACION DE LISTAS (pueden contener valores de cualquier tipo)
l1<-list("a",2,"c",23.3,TRUE)
print(l1)
l2<-list(list(list(1 , 3, 5))) #Tambien se pueden almacenar varias listas dentro de una lista

#Para saber que tipos de datos contiene la lista
str(list("a", 1L, 1.5, TRUE))

z <- list(list(list(1 , 3, 5)))
str(z)

#Tambien se le puede nombrar los valores (Key-value)
listaConNombres2<-list("Chicago" = 1, "New York" = 2, "Los Angeles" = 3)
#Para acceder por medio de los valores
listaConNombres2["Chicago"]
listaConNombres2["Los Angeles"]



