# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 09:11:10 2021

@author: CamiloDiazG
"""

#Funciones son las que toman algo de entrada y luego producen o cambian algo
#Funcion len devuelve el tamaño de entrada del argumento
s=[1,2,3,3,4,5]
len(s)

a="Hola"
len(a)

#Funcion sum devuelve la suma de los elementos en tuplas o listas
s2=[1.2,2,3,4.8]
sum(s2)

#Funcion sorted devuelve una lista ordenada de menos a mayor de los elementos de una lista
s3=[10,9,8,4,1,7,5,8,3,2,1]
newS3Sorted=sorted(s3)
print(newS3Sorted)

#Funcion sort organiza la lista que tiene los elementos
#La diferencia entre las dos es que sorted crea una nueva lista y sort organiza la misma
s3.sort()
print(s3)

##CREAR FUNCIONES
def add1(num):
    """
    Agrega al numero de entrada +1 
    """
    #Es recomendable documentar el codigo para que las personas que vayan a trabajar en este sepan que hace
    b=num+1
    return b

#Para llamar la funcion
add1(5)
#Tambien se puede asignar a una variable
c=add1(15)
print(c)

#Con la documentacion realizada entre los """ se puede obtener la documentacion
help(add1)

#Una funcion puede tener varias variables
def mult(num1,num2):
    """
    Multiplica el numero1 con el numero2
    """
    result=num1*num2
    return result

mult(10, 2) #Si los dos son int retornara int
mult(10,1.16) #Si uno es int y el otro float retornara float
mult(2,"Camilo ") #Si uno es int (Numero de veces) y el otro es String retornara el string multiplicado
# Esto para por que el simbolo * puede ser usado tambien en strings para multiplicar la secuencia

#Funciones que no retornaran nada (Python retornara el especial 'None')
def MJ():
    """
    Metodo que solo imprimira Michael Jackson
    """
    print ("Michael Jackson") #La funcion no retornara nada solo imprimira Michael Jackson

MJ() #Llamado de la funcion

#Funciones con pass
def noWork():
    pass #Se usara el keyword pass cuando se quiere pasar SIMILAR A BREAK de JAVA

print(noWork()) #Retornara none

#Las funciones pueden tener mas de una tarea
def add2(num1):
    num3=num1+2
    print(num1," mas 2 es igual a ",num3)
    return num3

add2(3)

def con(a, b):
    return(a + b)
con(['a', 1], ['b', 1])

#Tambien se pueden usar loops o whiles en las funciones
def printStuff(Stuff):
    for i,s in enumerate(Stuff): #i es el indice y s es el valor que contiene ese
        print("Album",i,"Ratings is",s)

album_ratings=[10,8.5,9.5]
printStuff(album_ratings)

#Otro ejemplo de for
def artistNames(*names): #Lleva el parentesis para el llamado de la funcion 
    for name in names:
        print(name)

artistNames("Michael Jacson","AC/DC","Pink Floyd") #Por el * los parametros se empaquetan en una TUPLA

#Alcance de una variable es la parte de una variable donde esta puede ser accedida
def addDC(x):
    x=x+"DC"
    print(x)
    return x
x="AC" #En este caso X es una variable global y puede ser accedida en cualquier parte de la funcion
z=addDC(x)

#Otro ejemplo de alcance
def Thriller():
    Date=1982
    return Date
Thriller()
#Date #Saltara error ya que Date esta definida dentro de la funcion y no es una variable global

#Solucion a lo anterior (Si es necesario)
def Thriller():
    Date=1982
    return (Date)
Date=2017
print(Thriller())
print(Date)

#Ejemplo de uso variable global y local
def ACDC(y):
    print(Rating) #No se definio esta variable en la funcion pero si es una variable global
    #Ver linea 128
    return(Rating+y)

Rating=9
defGloLo=ACDC(1)
print(Rating)
print(defGloLo)

#Otra manera para definir una variable global
def PinkFloyd():
    global ClaimedSales #Se define esta vairable como una global
    ClaimedSales="45 millions" #Se asigna el valor
    return ClaimedSales
PinkFloyd() #Se llama a la funcion
print(ClaimedSales) #Se puede acceder a la variable sin importar que se haya definido dentro de la funcion
