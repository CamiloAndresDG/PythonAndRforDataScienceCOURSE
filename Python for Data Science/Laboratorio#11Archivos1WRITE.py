# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 21:09:37 2021

@author: CamiloDiazG
"""
#Escribir en un archivo
with open ("archivoAEditar.txt","w") as file1: #El w+ sobreescribe todo lo que hayan en el archivo
    file1.write("Hola")
    file1.write(" como estan?\n")
    file1.write("Adios")
    
#De esta manera tambien se puede escribir en un archivo con una lista
Lines=["Esta es\n","la lista a","agregar"]
with open ("archivoAEditar.txt","w") as file1:
    for line in Lines:
        file1.write(line)
file1.close()

#Para copiar de un archivo a otro archivo
with open("ArchivoConTextoACopiar.txt","r") as file1:
    with open("ArchivoConTextoCopiado.txt","w") as file2:
        for line in file1:
            file2.write(line)
            
with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )

with open('Example2.txt', 'r+') as testwritefile: 
    data = testwritefile.readlines()
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    #testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())
    
#Finalmente, una nota sobre la diferencia entre w + y r +. 
#Ambos modos permiten el acceso a métodos de lectura y escritura, sin embargo, 
#abrir un archivo en w + lo sobrescribe y borra todos los datos preexistentes.
#Para trabajar con un archivo con datos existentes, use r + y a +. Mientras 
#usa r +, puede ser útil agregar un método .truncate () al final de sus datos. 
#Esto reducirá el archivo a sus datos y eliminará todo lo que sigue.