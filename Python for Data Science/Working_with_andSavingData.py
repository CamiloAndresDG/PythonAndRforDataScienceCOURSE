# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 22:13:17 2021

@author: CamiloDiazG
"""
import pandas as pd#Se importa la libreria pandas con el as pd se hace un apodo a pandas para el uso posterior

names={"Names":["Camilo","Roberth","Lina","Junior","Lyli","Daniel","Pipe","Juan"], 
       "LastNames":["Diaz","Diaz","Gomez","Diaz","Diaz","Castillo","Mendivelso","Contreras"], 
       "Year":[21,16,16,16,16,20,19,18]}
names_frame=pd.DataFrame(names)#Ahora se castea a un data frame
names_frame.head() #Se muestra

#Ahora si queremos tener una columna especifica del data frame anterior
x=names_frame[["Year"]] #Se obtiene solo la columna year
x.head() 

#Ahora si se quiere tener varias columnas
y=names_frame[["Names","LastNames"]]
y.head()

#Para sacar los valores unicos en la columna
names_frame["Year"] #De esta manera obtengo los datos de la columna year
names_frame["Year"].unique() #De esta manera tengo los datos sin repetir 

#Para sacar los valores dependiendo de una condicion (Retornara true o false)
#En este caso obtendre las personas que sean mayores a 18
names_frame["Year"]>18 #En este caso retornara la lista con los valores donde se cumple la condicion y donde no 
#Ahora si quiero obtener el resultado anterior en datos
names_frameNew=names_frame[names_frame["Year"]>=18]
names_frameNew.head()

#Ahora si quiero guardar el resultado final en un cvs
names_frameNew.to_csv("MayoresA18.csv") #Tambien hay mas formatos donde se puede exportar
