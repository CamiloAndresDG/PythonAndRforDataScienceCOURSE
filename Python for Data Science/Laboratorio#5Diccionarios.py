# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 22:07:59 2021

@author: CamiloDiazG
"""

#Los diccionarios son otro tipo de coleccion de datos
#La diferencia es (Las otras tienen indices y elementos) en Diccionarios hay (Key y valores)

diccionario={"Key1":1,"Key2":2}
print(diccionario)

diccionario2={"Thriller":1982,"Black in black":1980,"The dark side of the moon":1973}
print(diccionario2)

#Para obtener un valor del diccionario se hace con busqueda del key
print(diccionario2["Black in black"]) #Si no lo encuentra salta error

#Para agregar un valor en el diccionario
diccionario2["Graduation"]=2007
print(diccionario2)
diccionario2[2000]="Camilo"
print(diccionario2)

#Para eliminar un valor del diccionario se borra por el key
del(diccionario["Key1"])
print(diccionario)

#Para buscar un valor por medio del key
print("Thriller" in diccionario2)
print("Thriller2" in diccionario2) #Retornara false ya que no se encuentra Thriller2 en este diccionario

#Para obtener SOLAMENTE LOS KEYS del diccionario
print(diccionario2.keys())

#Para obtener SOLAMENTE LOS VALORES del diccionario
print(diccionario2.values())