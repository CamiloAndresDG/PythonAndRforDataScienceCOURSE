# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 14:44:14 2021

@author: CamiloDiazG
"""
"""Esto es para verificar en que ruta se encuentra el 
archivo con el que se esta trabajando"""

#import os
#cwd = os.getcwd()  # Get the current working directory (cwd)

#files = os.listdir(cwd)  # Get all the files in that directory
#print(files)

#Pandas: Carga de datos
import pandas as pd#Se importa la libreria pandas con el as pd se hace un apodo a pandas para el uso posterior
csv_file="airlines.csv"
df=pd.read_csv(csv_file) #Cargar un archivo csv y retornara un 
df.head() #Devuelve el data frame del cvs 

#De esta manera se cargan los datos para un archivo excel
#xlsx_file="Cleaned_2018_Flightsxyz.xlsx"
#da=pd.read_excel(csv_file) #Cargar un archivo csv y retornara un Data Frame
#da.head()#Devuelve el data frame del cvs 

#Tambien se puede crear un data frame desde un diccionario
#Las llaves son las columnas
#En este caso: Names, LastNames y Year
#Y los valores son la lista de filas
names={"Names":["Camilo","Roberth","Lina","Junior","Lyli"], 
       "LastNames":["Diaz","Diaz","Gomez","Diaz","Diaz"], 
       "Year":[21,16,16,16,16]}
names_frame=pd.DataFrame(names)#Ahora se castea a un data frame
names_frame.head() #Se muestra

#Ahora si queremos tener una columna especifica del data frame anterior
x=names_frame[["Year"]] #Se obtiene solo la columna year
x.head() 

#Ahora si se quiere tener varias columnas
y=names_frame[["Names","LastNames"]]
y.head()

#Ahora si se quiere acceder a un elemento en especifico
names_frame.iloc[1,1] #Obtiene de la segunda fila la segunda columna
names_frame.iloc[2] #Obtiene las columnas y filas del dato n°3
names_frame.iloc[:, 0] # Primera columna
names_frame.iloc[:, 1] # Segunda columna
names_frame.iloc[:, -1] # Última columna
#Tambien se puede por el nombre de la columna
#names_frame.iloc[1,"Names"]

#Los resultados de la busqueda anterior se pueden asignar a otro dataframe
#Ejmplo, se guardara en z el resultado del iloc, en este caso las filas 0,1
z=names_frame.iloc[0:2]
print(z)
