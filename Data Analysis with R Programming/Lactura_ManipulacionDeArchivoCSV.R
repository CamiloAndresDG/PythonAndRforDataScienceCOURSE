---
  title: "Lesson 3: Cleaning data"
output: html_document
---
  
## Background for this activity
  
## The scenario

# En este escenario, usted es un analista de datos junior que trabaja para una empresa de reservas de hoteles. Se te ha pedido que
#limpiar un archivo .csv que se creó después de consultar una base de datos para combinar dos tablas diferentes de diferentes
#hoteles. Para obtener más información sobre estos datos, necesitará utilizar funciones para obtener una vista previa de los datos.
#estructura, incluidas sus columnas y filas. También necesitará utilizar funciones básicas de limpieza para preparar este
#data para análisis. 

## Step 1: Load packages

#Para comenzar a limpiar sus datos, deberá instalar los paquetes requeridos.
#Si ya ha instalado y cargado `tidyverse`,` skimr` y `janitor` en esta sesión.

```{r}
install.packages("tidyverse")
install.packages("skimr")
install.packages("janitor")
```

# Una vez que se instala un paquete, puede cargarlo ejecutando la `biblioteca ()`
# función con el nombre del paquete entre paréntesis:

```{r}
library(tidyverse)
library(skimr)
library(janitor)
```

## Step 2: Import data


```{r}
bookings_df <- read_csv("hotel_bookings.csv")
```

## Paso 3: Conozca sus datos

#Antes de comenzar a limpiar sus datos, tómese un tiempo para explorarlos. Puedes usar
#varias funciones con las que ya está familiarizado para obtener una vista previa de sus datos,
#incluyendo la función `head ()` en el fragmento de código a continuación:

```{r}
head(bookings_df)
```

# También puede resumir u obtener una vista previa de los datos con `str ()` y `glimpse ()`
#functions para comprender mejor los datos ejecutando los siguientes fragmentos de código:


```{r}
str(bookings_df)
```

```{r}
glimpse(bookings_df)
```

# También puede usar `colnames ()` para verificar los nombres de las columnas en su conjunto de datos.
# Ejecute el fragmento de código a continuación para averiguar los nombres de las columnas en este conjunto de datos:

```{r}
colnames(bookings_df)
```

#Algunos paquetes contienen funciones más avanzadas para resumir y explorar su
#datos. Un ejemplo es el paquete `skimr`, que tiene varias funciones para este
#objetivo. Por ejemplo, la función `skim_without_charts ()` proporciona un resumen detallado
# de los datos. Intente ejecutar el siguiente código:

```{r}
skim_without_charts(bookings_df)
```

## Step 4: Cleaning your data

# Según las funciones que ha utilizado hasta ahora, ¿cómo describiría sus datos?
#en un resumen para sus partes interesadas? Ahora, digamos que está interesado principalmente en
#las siguientes variables: 'hotel', 'is_canceled' y 'lead_time'. Crear un nuevo
# marco de datos con solo esas columnas, llamándolo `trimmed_df` agregando los 
#nombres de las variables a este fragmento de código: 
 
 ```{r}
trimmed_df <- bookings_df %>% 
  select(is_canceled,lead_time, trimmed_df)
```

# Puede notar que algunos de los nombres de las columnas no son muy intuitivos, por lo que
# querrá cambiarles el nombre para que sean más fáciles de entender. Tu podrías querer
# cree el mismo marco de datos exacto que el anterior, pero cambie el nombre de la variable 'hotel' para que sea
# named 'hotel_type' para ser muy claro sobre de qué se tratan los datos

#Complete el espacio a la izquierda del símbolo '=' con el nuevo nombre de la variable:

```{r}
trimmed_df %>% 
  select(hotel, is_canceled, lead_time) %>% 
  rename(hotel_type = hotel)
```

#Otra tarea común es dividir o combinar datos en diferentes columnas. En este ejemplo, 
#puede combinar el mes y el año de llegada en una columna usando la función unite ():

  ```{r}
example_df <- bookings_df %>%
  select(arrival_date_year, arrival_date_month) %>% 
  unite(arrival_month_year, c("arrival_date_month", "arrival_date_year"), sep = " ")
```

## Step 5: Another way of doing things

#También puede usar la función`mutate () `para realizar cambios en sus columnas. 
#Supongamos que desea crear una nueva columna que resuma todos los adultos, niños 
#y bebés de una reserva para el número total de personas. Modifique el fragmento de 
#código a continuación para crear esa nueva columna:  

    ```{r}
example_df <- bookings_df %>%
  mutate(guests = people)

head(example_df)
```

#Excelente. ¡Ahora es el momento de calcular algunas estadísticas resumidas! 
#Calcule el número total de reservas canceladas y el tiempo medio de espera para 
#la reserva; querrá comenzar su código después del símbolo%>%. Cree una columna 
#llamada 'número_cancelado' para representar el número total de reservas canceladas. 
#Luego, cree una columna llamada 'average_lead_time' para representar el tiempo de 
#entrega promedio. Use la función `resume ()` para hacer esto en el fragmento de código a continuación:  

    ```{r}

example_df <- bookings_df %>% resume()
  
  
  head(example_df)
```


