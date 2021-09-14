# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 15:38:42 2021

@author: CamiloDiazG
"""
##SETS
#Es un tipo de coleccion como las tuplas y listas
#No tiene organizacion, es decir, no tiene indices
#Los elementos en el set no se repiten
set1={"rock","pop","rock","jazz","rock","clasica"} #Se repite rock varias veces
print(set1) #No estara rock repetido
print(len(set1))

#Se puede convertir de una lista a un set
list1=["Camilo","Andres","Diaz","Gomez","Camilo"]
print(list1)
setLista=set(list1)
print(setLista)

abecedario={"a","b","c","h","e","z","m"}
print(abecedario)
abecedario.add("d")
print(abecedario)

abecedario.remove("h") #De esta manera se elimina el elemento que sea igual al argumento de entrada
print(abecedario)

print("c" in abecedario) #Se verifica si c esta dentro del set abecedario
print("ñ" in abecedario) #Se verifica si ñ esta dentro del set abecedario

##VERIFICAR CUADRO DE VENN (OPERACIONES ENTRE CONJUNTOS)
abecedario2={1,2,3,4,5,"c","h","e"}
#SE HARA UNA INTERSECCION EN LOS DOS SETS
set3=abecedario&abecedario2 #O set3=abecedario.intersection(abecedario2)
print(set3) #Se imprimira los valores que se repiten en los dos sets (INTERCEPCION)

#TAMBIEN SE PUEDE REALIZAR UNIONES
set3=abecedario.union(abecedario2)
print(set3)

#DE IGUAL MANERA SE PUEDEN HACER DIFERENCIAS
set3=abecedario.difference(abecedario2)
print("-----")
print(set3)

#PARA SABER SI UN SET ESTA DENTRO DE OTRO SET (SUBSET)
prueba1={3}
prueba2={3,4,5}
print(prueba1.issubset(prueba2)) ##Devolveria true ya que 3 esta dentro del set prueba2

##Metodo que suma los numeros dentro del set
setSuma={1,2,3,4,5}
print(sum(setSuma))