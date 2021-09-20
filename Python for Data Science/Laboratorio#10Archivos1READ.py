# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 14:59:13 2021

@author: CamiloDiazG
"""

#Crear un objeto file y obtener los datos dentro de este

#Para acceder al archivo
file1=open("archivoPrueba.txt","w") #El ultimo argumento
#Puede ser r=reading, w=writing o a=appending

#Metodos para la clase file
file1.name #Obtiene el nombre del archivo
file1.mode #Obtiene el modo al que se esta accediendo 
file1.close() #Siempre se tiene que cerrar el archivo

#DECLARACION with
with open("archivoPrueba2.txt","r") as F1: #Con el archivo abierto se ejecuta lo siguiente
    file_stuff=F1.read() #Guarda todo los valores que estan en F1 a file_stuff como un string
    print(file_stuff)
print(F1.closed)
print(file_stuff)

#Agregar cada linea en una lista
with open("archivoPrueba2.txt","r") as F1: #Con el archivo abierto se ejecuta lo siguiente
    file_stuff2=F1.readlines() #Guarda todo los valores que estan en F1 a file_stuff como un string
    print(file_stuff2)
print(F1.closed)
print(file_stuff2)

#Agregar la primera linea en una lista
with open("archivoPrueba2.txt","r") as F1: #Con el archivo abierto se ejecuta lo siguiente
    file_stuff2=F1.readline() #Guarda todo los valores que estan en F1 a file_stuff como un string
    print(file_stuff2)
    file_stuff2=F1.readline()
    print(file_stuff2)
print(F1.closed)
print(file_stuff2)

#Tambien se puede imprimir cada linea con un for
with open("archivoPrueba2.txt","r") as F1:
    for line in F1:
        print(line)
        
#Podemos especificar el numero de caracteres que nos gustaria ver
with open("archivoPrueba2.txt","r") as F1:
    file_stuff3=F1.readline(17) #En este caso, se detuvo en la pos 17 del String
    print(file_stuff3)
    file_stuff3=F1.readline(2) #Aqui retomara la pos 18 por el anterior uso
    print(file_stuff3)
        

