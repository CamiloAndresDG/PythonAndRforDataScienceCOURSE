# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:25:33 2021

@author: CamiloDiazG
"""


name="Camilo Andres"
print(name[0:4])#Imprime los valores de la pos 0 a 4
print(name[::2])#Imprime los valores que se encuentren cada 2 casillas
print(name[0:10:2])#Imprime los valores de la pos 0 a la 10que esten cada 2 casillas
print(len(name))#Obtener el tamaño
full_name=name+" Diaz Gomez"
print(full_name)

print(3*full_name)##Imprime 3 veces el nombre completo

full_name=name+" Diaz Gomez"+"\nme presento"#ENTERS
print(full_name)

full_name=name+" Diaz Gomez"+"\tme presento"#TABS
print(full_name)

print("\\\\") #backslash
print(r"\ ") #backslash

uper_case=name.upper() #Poner todo en mayuscula
print(uper_case)
lower_case=name.lower() #Poner todo en minuscula
print(lower_case)

replace=name.replace("Camilo", "Camilo2") #Cambiar una parte del String por otra
print(replace)

print(name.find("lo")) #Imprime donde empieza la parte "lo" de mi nombre
print(name.find("Andres")) #Imprime donde empieza mi segundo nombre
print(name.find("XYZ")) #Como no esta en el nombre imprime un valor negativo
