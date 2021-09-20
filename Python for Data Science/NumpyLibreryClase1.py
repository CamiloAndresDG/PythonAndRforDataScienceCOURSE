# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 12:17:28 2021

@author: CamiloDiazG
"""

#NumpyClase1
#Numpy proporciona velocidad y mejor manejo de memoria
#Numpy son las bases de Pandas

#Crear un array
a=["0",1,"two","3",4]
a[0] #Se accede a la primera posicion
a[-1] #Se accede a la ultima posicion
a[2] #Se acede a la tercera pos

import numpy as np
#Un numpy array siempre tiene en todos sus elementos el mismo tipo de dato
b=[1,2,3,4,5]
B=np.array(b) #Tambien se puede comoB=np.array([1,2,3,4,5])

B[1]#Accedo a la segunda pos del numpy array

#Para obtener el tipo de dato del numpy array
type(B)

#Para obtener los tipos de datos que se manejan en el numpy array
B.dtype

#Para obtener el tamanio del numpy array
B.size

#Para obtener el numero de dimensiones del array
B.ndim #En este caso me trae 1 pero si dentro del array hubieran mas traeria el numeor de arrays concatenados (VER EXPLICACION EN CLASE2)

#Para obtener el tamaño de las dimensiones (SE DEVUELVE EN UNA TUPLA)
B.shape 

#Otro ejemplo de Numpy array
c=np.array([1.2,1.2,1.3])
type(c)
c.dtype 


############
#Indexing y Slicing methods
d=np.array([20,1,2,3,4]) #Se crea el numpy array
d #Se imprime
d[0]=100 #De la pos 0 se cambia a 100
d #se vuelve a imprimir
d[3]=200
d
#Tambien podemos agregar varios valores
d[1:5]=200,100,50,20 

#Podemos hacer slice
e=d[1:4] #Trae desde la segunda pos hasta la 4 pos
e


####
#Adicion y substraccion de los vectores
u=np.array([1,0])
v=np.array([0,1])
z=u+v #Se sumanlos valores dependiendo del indice, EJ: indice 1 con indice 1
print(z)
#ES LO MISMO QUE:
"""
u=[1,0]
v=[0,1]
z=[]
for n,m in zip(u,v):
   z.append(n+m)
""" #Pero ahorra mas memoria y timepo de ejecucion

#Subtraccion o resta
zRes=u-v
zRes
#ES LO MISMO QUE:
"""
u=[1,0]
v=[0,1]
z=[]
for n,m in zip(u,v):
   z.append(n-m)
""" #Pero ahorra mas memoria y timepo de ejecucion

#Multiplicación de matrices con un escalar
y=np.array([1,2])
y_2=2*y #Cada componente del vector es multiplicado por 2
y_2
#ES LO MISMO QUE:
"""
y=[1,2]
z=[]
for n in y:
   z.append(2*n)
""" #Pero ahorra mas memoria y timepo de ejecucion        

#Producto entre dos numpy arrays
u=np.array([1,2])
v=np.array([3,2])
z=u*v #Se multiplica 1*3 y 2*2
z
#ES LO MISMO QUE:
"""
u=[1,2]
v=[3,2]
z=[]
for n,m in zip(u,v):
   z.append(n*m)
""" #Pero ahorra mas memoria y timepo de ejecucion

#Producto escalar
u=np.array([1,2])
v=np.array([3,1])
result=np.dot(u,v) #Se multiplican entre si en los indices y suma los valores
result

#Suma escalar
u=np.array([1,2,-1,-2,5])
z=u+2 #Se le suma a cada +2
z

#UNIVERSAL FUNCTIONS
#Promedio
u=np.array([1,2,3,4,5])
mean_u=u.mean() #Mean sirve para traer el promedio de numeros del numpy array
mean_u

#Numero mayor en el array
u=np.array([1,2,10,4,5])
max_u=u.max()
max_u

#Pi y seno (Funicones trigonometricas) en Numpy
pi_n=np.pi
x=np.array([0,pi_n/2,pi_n]) #Imrprime los valores en pi
x
y=np.sin(x) #A los valores de pi se saca seno
y

##FUNCIONES PARA OBTENER UN RANGO DE NUMEROS EN UN INTERVALO
lista1=np.linspace(-2, 2,num=5)
lista1 #En este caso se genera una lsita de numeros desde el -2 al 2
#Teniendo en cuenta que elegi imprimir 5 numeros no mas, por eso, son enteros

lista2=np.linspace(-2,2,num=9)
lista2 #En este caso se genera una lsita de numeros desde el -2 al 2
#Teniendo en cuenta que elegi imprimir 9 numeros no mas, por eso, tiene decimales

#OTRO EJEMPLO
#Voy a general numeros del 0 al 2pi
x=np.linspace(0,2*pi_n,100) #Obtengo 100 numeros desde el 0 al 2*pi
y=np.sin(x) #Se mapea el array x a y pero con seno

import matplotlib.pyplot as plt #Se importa para mostrar la funcion
plt.plot(x,y) #Se imprime la funcion de Seno
#x=valores de x y y=valores de y




