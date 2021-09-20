# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 14:38:16 2021

@author: CamiloDiazG
"""

#Que es una excepcion?
#Una excepción es un error que ocurre durante la ejecución del código. 
#Este error hace que el código genere una excepción y, si no está preparado 
#para manejarlo, detendrá la ejecución del código.

#1/0 #Esto causa un error por que no se puede dividir entro 0 (division by zero)
#y = a + 5 #Esto causa un error por que no esta definido la variable a (NameError)
#a = [1, 2, 3]
#a[10] #Esto causa un error por que la lista no tiene un tamaño de 10 (IndexError)

#Como se puede controlar las excepciones
try:
    print("A") # code to try to execute
except:
    print("B") # code to execute if there is an exception
    
a = 1
try:
    b = int(input("Please enter a number to divide a")) #Se pide el numero para dividir
    a = a/b
    print("Success a=",a)
except:
    print("There was an error") #Si hay un error, por ejemplo (b=0)

#Un intento específico excepto le permite detectar ciertas excepciones y 
#también ejecutar cierto código dependiendo de la excepción.

try:
    # code to try to execute
except (ZeroDivisionError, NameError):
    # code to execute if there is an exception of the given types

#ES LO MISMO A 

# potential code before try catch
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError

#TAMBIEN AGREGANDO UN EXCEPT A LO ULTIMO 
#También puede tener un vacío excepto al final para detectar una excepción 
#inesperada

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception

###EJEMPLO DE LO ANTERIOR
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")

#Ahora si se quiere comrbobar que no hay ningun error
#else permite comprobar si no hubo ninguna excepción al ejecutar el bloque try.
#Esto es útil cuando queremos ejecutar algo solo si no hubo errores.
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
    
###EJEMPLO DE LO ANTERIOR
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)

#Ahora si se quiere realizar una parte de codigo si o si salga una excepcion
#finally nos permite ejecutar siempre algo, incluso si hay una excepción o no. 
#Esto se usa generalmente para significar el final del intento, excepto.
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
finally:
    # code to execute at the end of the try except no matter what

###EJEMPLO DE LO ANTERIOR
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")