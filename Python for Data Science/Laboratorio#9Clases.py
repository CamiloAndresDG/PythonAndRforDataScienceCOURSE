# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 11:05:28 2021

@author: CamiloDiazG
"""

#Los objetos tienen
 #Un tipo
 #Una representacion interna de los datos
 #Un conjunto de procedimientos para interactuar con los datos (metodos)
#Un objeto es una instancia de un tipo particular
 #Por ejemplo cada vez que se crea un int es una instancia del tipo Integer
int1=20 #Es una instancia del tipo Integer=5 objetos tipo integer
list1=[1,2,3,4] #Se esta creando una instancia del tipo list=lista de tipo List

#Para saber el tipo del objeto se utiliza el comando
type(list1)
type(int1)
type("Hola")

#Los metodos de una clase son funciones que toda instancia de la clase o tipo provee
#Es como se interactua con los datos en un objeto
#Por ejemplo en una lista, el metodo sorted interactua con los datos de la lista
#Para organizalos de menor a mayor  
ratings=[10,9,1,10,5,3,1,3]
ratings.sort()  #Metodo para organizarlo de menor a mayor
print(ratings)

[10,9,1,10,5,3,1,3].sort() #Tambien se puede asi

ratings.reverse() #Metodo para organizarlo de mayor a menor
print(ratings)

##CREACION DE CLASES
