# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 10:55:53 2021

@author: CamiloDiazG
"""

#Numpy
#Podemos crear arrays numpy con mas de una dimension
#En este caso se crearan numpy arrays 2D pero se pueden crear de mas

import numpy as np#Se importa
#Consideremos la lista
a=[[11,12,13],
   [21,22,23],
   [31,32,33]]


#Podemos castear la lista a numpy
A=np.array(a)
print(A)

A.ndim #Retornara el numero de dimensiones de la matriz

#En Matemáticas/Física, la dimensión o dimensionalidad se define informalmente 
#como el número mínimo de coordenadas necesarias para especificar cualquier
#punto dentro de un espacio. Pero en Numpy, de acuerdo con numpy doc , es lo 
#mismo que ejes/ejes:
#En numpy las dimensiones se llaman ejes. El número de ejes es rango.

#Otro ejemplo
b=[[[1.1,1.2,1.2],[2.1,2.2,2.3],[3.1,3.2,3.3]],
   [[4.1,4.2,4.3],[5.1,5.2,5.3],[6.1,6.2,6.3]],
   [[7.1,7.2,7.3],[8.1,8.2,8.3],[9.1,9.2,9.3]]]
B=np.array(b)
print(B)

B.ndim #En este caso hay 3 dimensiones



#Para la representacion
A.shape #(3,3)Me retornara cuantas listas anidadas hay 
#Y el segundo valor corresponde al tamanio de cada lista

#Para ver el tamanio
A.size #Multiplica las filas y las columnas para obtener el tamanio (3x3)

#DE ESTA MANERA SE REPRESENTAN LAS POSICIONES EN LA MATRIZ
c=[["A[0,0]","A[0,1]","A[0,2]"],
   ["A[1,0]","A[1,1]","A[1,2]"],
   ["A[2,0]","A[2,1]","A[2,2]"]] #[x,x] El primer valor corresponde a la fila y el segundo corresponde a la columna

C=np.array(c)
print(C)

C[1,2] #Podemos obtener el valor que esta dentro de la fila 1 y la columna 2

#Otro ejemplo
A[1,2]

#Tambien podemos obtener varios valores
A[0,0:2] #Me devuelve de la primera fila las dos primeras columnas
A[2,0:3] #Me devuelve de la tercera fila las tres columnas
A[1] #Me devuelve la segunda fila de la matriz
print(A[0][0:2]) #Me devuelve de la primera fila las dos primeras columnas o datos
print("_-------------------")


#Otro ejemplo para obtener los datos de forma vertical (columnas) VERIFICAR
A[0:2,2] #[0:2]Corresponden a las dos ultimas filas #[2,2]Corresponden a la ultima columna

#Podemos hacer sumas en las matrices como algebra
X=np.array([[1,0],[0,1]]) #Para agregar arrays en numpy
Y=np.array([[2,1],[1,2]]) #Para agregar arrays en numpy

Z=X+Y #Se suma como en algebra linearl los valores 
print(Z)

#Tambien podemos hacer multiplicaciones escalares
Y_2=2*Y
print(Y_2) #Cada elemento se multiplica por 2

#Tambien podemos sacar el producto entre dos matrices
#En este caso cada posicion de las matrices se multiplican entre si
#Por ejemplo, la pos del x(0,0) se multiplcia con y(0,0)
X_Y=X*Y#Devuelve una matriz
print(X_Y) #Multiplica cada elemento con el elemento correspondiente de la otra matriz, como en algebra lineal

#Producto escalar entre matrices
A=np.array([[0,1,1],[1,0,1]]) #Matriz de tamanio (2x3) Dos filas y tres columnas
B=np.array([[1,1],[1,1],[-1,1]]) #Matriz de tamanio (3x2) Tres filas y dos columnas
C=np.dot(A,B)

#Tambien podemos calcular el seno de cada elemento (Tambien hay secante, tangente,etc)
print(np.sin(C)) #Calcula el seno de cada elemento

#Tambien podemos obtener la matriz transpuesta (Como en algebra)
print(C.T)

#Para obtener el tipo de dato que hay dentro de la matriz
A.dtype
B.dtype


