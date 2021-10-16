
## The Scenario
#In this scenario, you are a junior data analyst working for a hotel booking company. You have been asked to clean a .csv file that was created after querying a database to combine two different tables from different hotels. You have already performed some basic cleaning functions on this data; this activity will focus on using functions to conduct basic data manipulation.

## Step 1: Load packages

# Empiece por instalar los paquetes necesarios. Si ya ha instalado y cargado `tidyverse`,` skimr` y `janitor` en esta sesión, no dude en omitir los fragmentos de código en este paso. Esto puede tardar unos minutos en ejecutarse y es posible que aparezca una ventana emergente que le pregunte si desea continuar. Haga clic en sí para continuar instalando los paquetes.
```{r install packages}
install.packages("tidyverse")
install.packages("skimr")
install.packages("janitor")
```

#Once a package is installed, you can load it by running the `library()` function with the package name inside the parentheses:
  
  ```{r load packages}
library(tidyverse)
library(skimr)
library(janitor)
```

## Step 2: Import data

#En el fragmento de abajo, usará la función `read_csv ()` para importar datos desde un .csv en la carpeta del proyecto llamada "hotel_bookings.csv" y guardarlo como un marco de datos llamado `hotel_bookings`.

#Si esta línea causa un error, cópiela en la línea setwd ("proyectos / Curso 7 / Semana 3") antes.

# Escriba el nombre del archivo en el lugar correcto para leerlo en su consola R: 
  
  ```{r load dataset}
hotel_bookings <- read_csv("")
```

## Step 3: Getting to know your data

#Como ha estado haciendo en otros ejemplos, utilizará funciones de resumen para conocer sus datos. Esta vez, completará los fragmentos de código 
#a continuación para utilizar estas diferentes funciones. Puede utilizar la función `head ()` para obtener una vista previa de las columnas y las 
#primeras filas de datos. Termine el fragmento de código a continuación y ejecútelo:  
 
 ```{r head function}
head()
```
### Practice Quiz 

1. How many columns are in this dataset?
  A: 45
B: 100
C: 32
D: 60

#2. The 'arrival_date_month' variable is chr or character type data.  
A: True
B: False

#Ahora sabe que este conjunto de datos contiene información sobre reservas de hotel. Cada reserva es una fila en el conjunto de datos y cada columna contiene información como qué tipo de hotel se reservó, cuándo se realizó la reserva y con qué anticipación tuvo lugar (la columna 'lead_time').

#Además de `head ()` también puede usar las funciones `str ()` y `glimpse ()` para obtener resúmenes de cada columna en sus datos organizados horizontalmente. Puede probar estas dos funciones completando y ejecutando los fragmentos de código a continuación:
  
  ```{r str function}
(hotel_bookings)
```

# Puede ver los diferentes nombres de columna y algunos valores de muestra a la derecha de los dos puntos.

```{r glimpse function}
glimpse()
```

# También puede usar `colnames ()` para obtener los nombres de las columnas en su conjunto de datos. Ejecute el fragmento de código a continuación para obtener los nombres de las columnas:

  ```{r colnames function}
colnames(hotel_bookings)
```

## Manipulating your data

# Supongamos que desea organizar los datos por mayor tiempo de espera al menor tiempo de espera porque desea centrarse en las reservas que se realizaron con mucha anticipación. Decide que quiere intentar usar la función `arreglar ()`; ingrese el nombre correcto de la columna después de la coma y ejecute este fragmento de código:

```{r arrange function}
arrange(hotel_bookings, )
```


# ¿Pero por qué hay tantos ceros? Esto se debe a que `organizar ()` ordena automáticamente en orden ascendente, y usted necesita indicarle específicamente cuándo ordenar en orden descendente, como el siguiente fragmento de código a continuación:

  ```{r arrange function descending} 
arrange(hotel_bookings, desc(lead_time))
```

#Ahora está en el orden que necesitaba. También puede hacer clic en las diferentes páginas de resultados para ver filas de datos adicionales.

## Practice Quiz
What is the highest lead time for a hotel booking in this dataset?
  A: 737
B: 709
C: 629
D: 0

#Tenga en cuenta que cuando simplemente ejecuta `arrange ()` sin guardar sus datos en un nuevo marco de datos, no altera el marco de datos existente. Compruébelo ejecutando `head ()` nuevamente para averiguar si los tiempos de entrega más altos son los primeros:
  
  ```{r head function part two}
head(hotel_bookings)
```

# Esto se aplicará a todas las funciones que utilizará en esta actividad. Si quisiera crear un nuevo marco de datos que tuviera esos cambios guardados, usaría el operador de asignación, <-, como está escrito en el fragmento de código a continuación para almacenar los datos organizados en un marco de datos llamado 'hotel_bookings_v2':

  ```{r new dataframe}
hotel_bookings_v2 <-
  arrange(hotel_bookings, desc(lead_time))
```

Run `head()`to check it out: 
  
  ```{r new dataframe part two}
head(hotel_bookings_v2)
```

#También puede averiguar los plazos de entrega máximos y mínimos sin ordenar todo el conjunto de datos utilizando la función `arrange ()`. Pruébelo usando las funciones max () y min () a continuación:  
 
 ```{r}
max(hotel_bookings$lead_time)
```

```{r}
min(hotel_bookings$lead_time)
```

# Recuerde, en este caso, debe especificar qué conjunto de datos y qué columna usando el símbolo $ entre sus nombres. Intente ejecutar lo siguiente para ver qué sucede si olvida una de esas piezas:  
  ```{r}
min(lead_time)
```

#Este es un error común que encuentran los usuarios de R. Para corregir este fragmento de código, deberá agregar el marco de datos y el signo de dólar en los lugares apropiados.

#Ahora, digamos que solo desea saber cuál es el tiempo de espera promedio para la reserva porque su jefe le pregunta con qué anticipación debe ejecutar promociones para habitaciones de hotel. Puede usar la función `mean ()` para responder esa pregunta ya que el promedio de un conjunto de números también es la media del conjunto de números:```{r mean}

mean(hotel_bookings$lead_time)
```

#Debería obtener la misma respuesta incluso si usa el conjunto de datos v2 que incluye la función `arreglar ()`. Esto se debe a que la función `arreglar ()` no cambia los valores en el conjunto de datos; simplemente los reorganiza.

```{r mean part two}
mean(hotel_bookings_v2$lead_time)
```

## Practice Quiz 
What is the average lead time?
  A: 100.0011
B: 45.0283
C: 14.0221
D: 104.0114

#Pudiste informarle a tu jefe cuál es el tiempo de espera promedio antes de reservar, pero ahora ellos quieren saber cuál es el tiempo de espera promedio antes de reservar solo para los hoteles de la ciudad. Quieren enfocar la promoción que están realizando dirigiéndose a las principales ciudades.

#Sabe que su primer paso será crear un nuevo conjunto de datos que solo contenga datos sobre hoteles urbanos. Puedes hacerlo usando la función `filter ()` y nombrar tu nuevo marco de datos 'hotel_bookings_city':

```{r filter}
 <- 
  filter(hotel_bookings, hotel_bookings$hotel=="City Hotel")
```

Check out your new dataset:

```{r new dataset}
head(hotel_bookings_city)
```

#Verifica rápidamente cuál es el tiempo de entrega promedio para este conjunto de hoteles, tal como lo hizo antes para todos los hoteles:

  ```{r average lead time city hotels}
mean(hotel_bookings_city$lead_time)
```

#Ahora, su jefe quiere saber mucha más información sobre los hoteles de la ciudad, incluido el tiempo de entrega máximo y mínimo. También les interesa en qué se diferencian de los hoteles vacacionales. No desea ejecutar cada línea de código una y otra vez, por lo que decide utilizar las funciones `group_by ()` y`summarize () `. También puede utilizar el operador de tubería para que su código sea más fácil de seguir. Almacenará el nuevo conjunto de datos en un marco de datos llamado 'hotel_summary':  

  ```{r group and summarize}
hotel_summary <- 
  hotel_bookings %>%
  group_by(hotel) %>%
  summarise(average_lead_time=mean(lead_time),
            min_lead_time=min(lead_time),
            max_lead_time=max(lead_time))
```

Check out your new dataset using head() again:
  
  ```{r}
head(hotel_summary)
```