#Lubridate package es una libreria para el uso de fechas y tiempos en R
install.packages("tidyverse") #Se instala el paquete donde viene el lubridate
library(tidyverse) #Se carga la libreria
library(lubridate) #Se carga finalmente la libreria de lubridate
#In R, there are three types of data that refer to an instant in time:
 # A date ("2016-08-16")
 # A time within a day (“20:11:59 UTC") (UTC=Universal Time Coordinated)
 # And a date-time. This is a date plus a time ("2018-03-31 18:15:48 UTC")

#Para tener la fecha actual
today() #Date

#Para obtener el date-time
now() #Date-time

#When working with R, there are three ways you are likely to create date-time formats: 
 # From a string
 #From an individual date
 #From an existing date/time object
 ##R creates dates in the standard yyyy-mm-dd format by default. 

#Para convertir a date
ymd("2021-09-14")
mdy("September 14th, 2021")
dmy("14-Sep-2021")
ymd(20210914)
as_date(now())#Tambien se puede convertit un date-time a date

#Para convertir a date-time
ymd_hms("2021-09-14 12:00:59")
mdy_hm("09/14/2021 12:01")
