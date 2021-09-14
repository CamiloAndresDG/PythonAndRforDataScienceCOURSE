# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

###TUPLAS
##Las tuplas son una secuencia ordenada
ratings=(10,9,6,5,10,8,9,6,2)

tuple1=("Disco",1,1.1) #Puede contener diferentes tipos de datos

type(tuple1) #El tipo de la tupla es tuple

tuple1[0] #Se accede al indice 1 de la tupla
tuple1[-3] #Tambien s epuede acceder por los indices negativos, de derecha a izquierda

#Para concatenar tuplas
tuple2=tuple1+("de Hard Rock",98.676,2)
print(tuple2)

print(3*tuple1) #Tambien como los String se puede multiplicar las tuplas para repetir su contenido

print(tuple2[0:3]) #Para acceder a los 3 primeros indices de la tupla 2
#El segundo indice tiene que ser +1 al que queremos llegar
print(tuple2[3:6])

print(len(tuple2)) #Para obtener el tamaño de la tupla
print(len(("Disco",1,1.1)))

##Las tuplas son inmutables, lo que significa que no podemos cambiarlas
ratings1=ratings
#ratings1[1]=2 #NO funciona por que no se pueden cambiar
#De la unica manera que podramos manipular la tupla es asignandola a otra con lo que queremos
ratingsSorted=sorted(ratings) #Por ejemplo se ordena de menor a mayor
print(ratingsSorted)

#Dentro de una tupla pueden haber muchas tuplas
tupla3=(1,2,("Pop","Rock"),(3,4),5,6,("Disco","Plata"))
tuplaExtraccion=tupla3[2]
print(tuplaExtraccion[1]) #De esta manera se accede al indice 1 del indice 2
#Otra forma
print(tupla3[2][1]) #Es lo mismo pero simplificado
#Para obtener un caracter dentor de las tuplas
print(tupla3[2][1][2]) #Obtengo la letra que esta ubicada en la pos 2 del indice 1 del 2

###LISTAS
##Las listas son una secuencia ordenada
##Las listas son mutables, lo que significa que podemos cambiarlas
lista=[1,2.2,"Camilo Diaz"]

#Lista con diferentes tipos de datos
listaExtendida=[1,2,3.333,["Camilo","Diaz"],("Andres","Gomez")]
print(listaExtendida[3])
print(listaExtendida[-2])#Tambien se puede acceder con indices negativos
print(listaExtendida[2:4])

#Para concatenar o adicionar listas
listaConcatenada=lista+listaExtendida+[2,3,["Concatenado","Plus"]]
print(listaConcatenada)
#Ota manera con un metodo
listaConcatenada.extend(["Esta es ","La otra manera"]) #Esta agrega como tal nuevos indices a la lista
print(listaConcatenada)
#Otra manera
listaConcatenada.append(["Aqui estoy agregando","Otra lista"]) #Esta agrega exactamente lo que esta dentro de los parentesis
print(listaConcatenada)
listaConcatenada.append("Ultimo indice") #Esta agrega como tal un indice ya que es lo que esta dentro de los parentesis 
print(listaConcatenada)

#Ahora para eliminar un elemento de una lista
del(lista[1])
print(lista)

#Para convertir un String a una lista separado por los espacios
stringALista="Camilo Andres Diaz Gomez"
listaNombre=stringALista.split()
print(listaNombre)
#Tambien se puede separar por otros argumentos, ejemplo, por comas
stringALista="Ayer llovio,aun asi,salimos a montar bicicleta"
listaNueva=stringALista.split(",")
print(listaNueva)

#Para copiar una lista
lista1=[1,2,3,4] #Lista de numeros del 1 al 4
lista2=lista1 #Se copia exactamente (Si hay algun cambio, la lista 2 lo tomara)
#Esto sucede ya que los dos referencian a la misma lista
print(lista2)
lista1[0]=0 #Se cambia el indice 0 a 0
print(lista2) #Se puede observar que cambia
#Si se quiere copiar una lista sin ser alterada a futuro se tiene que hacer lo siguiente
lista3=lista1[:]
lista1[1]=0
print(lista3) #Aqui se puede observar que a pesar del cambio en la lista 1 no se altero la lista 3
print(lista1) #Lista 1
print(lista2) #Aqui s epuede observar que se cambio la lista 2 por el cambio en la lista1

#Para buscar un elemento en una lista
print(listaNueva.index("aun asi"))

#Para obtener ayuda y saber los metodos que hay dentro de la clase
help(lista1)
