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

###############################################################################

##CREACION DE CLASES
#Las clases tienen atributos y metodos
#Despues podemos crear diferentes instancias de la clase creada 

#Para este curso de Python se pondra object dentro de los parentesis
#Object es la clase madre de Circle
class Circle (object): #----Se define la clase
  kind = "figure" # class variable shared by all instances
 #La funcion _init_ es un metodo o contructor espacial para inicializar los atributos de los datos (the data atributes)  
  def __init__(self,radius,color): #---Se crea la contructora de la clase y se inicializan cada isntancia de la clase
 #El parametro self se referencia a la instancia de la clase recien creada (Similar a this de Java)
        self.radius=radius;
        self.color=color;
  def addRaduis(self,radius):
      self.radius=self.radius+radius
  #def drawCircle(self):
      
      
      
#Object es la clase madre de Rectangule
class Rectangule (object): #----Se define la clase
 #La funcion _init_ es un metodo o contructor espacial para inicializar los atributos de los datos (the data atributes)  
     def __init__(self,color,height,width): #---Se crea la contructora de la clase y se inicializan cada isntancia de la clase
 #El parametro self se referencia a la instancia de la clase recien creada (Similar a this de Java)
        self.color=color;
        self.height=height;
        self.width=width;
    
BlueCircle=Circle(10,"Blue") #Tambien se puede BlueCircle=Circle(color="Blue",radius=10)

BlueCircle.color
BlueCircle.color="Light Blue"
BlueCircle.addRaduis(10)
print(BlueCircle.radius)

RedCircle=Circle(5,"Red")
RedCircle.radius
RedCircle.kind

WhiteRectangule=Rectangule("White", 2, 2)
WhiteRectangule.height
WhiteRectangule.color="Gray"

#Para ver lo que esta asociado a la clase (Clases, metodos, entre otros)
dir(BlueCircle)