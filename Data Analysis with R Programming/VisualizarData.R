```{r}
install.packages("tidyverse") #Se instala el paquete
```

```{r}
library(tidyverse) #Se carga el paquete
```

# Step 2: Viewing data


```{r}
head(diamonds) #Metodo para previsualizar los datos
```

#Adem�s de `head ()` hay una serie de otras funciones �tiles que puede utilizar 
#para resumir o obtener una vista previa de los datos. Por ejemplo, las funciones 
#`str ()` y `glimpse ()` devolver�n res�menes de cada columna de sus datos 
#dispuestos horizontalmente.

```{r}
str(diamonds)
```

```{r}
glimpse(diamonds)
```
#Otra funci�n simple que puede usar con regularidad es la funci�n `colnames ()`. 
#Devuelve una lista de nombres de columna de su conjunto de datos. 

```{r}
colnames(diamonds)
```

## Step 3: Cleaning data
#Siempre sera necesario hacer limpieza de datos

```{r}
#Por ejemplo, es posible que deba cambiar el 
#nombre de las columnas o variables en sus datos.
#Hay una funci�n para eso: `rename ().`
rename(diamonds, carat_new = carat) #En este caso cambia de carat a carat_new
```

```{r}
rename(diamonds, carat_new = carat, cut_new = cut) #En este caso se cambia el nombre a mas de una columna
```

```{r}
#Otra funci�n �til para resumir sus datos es "resume ()". Puede usarla para 
#generar una amplia gama de estad�sticas resumidas para sus datos. 
#Por ejemplo, si desea saber cu�l es la media de `carat` en este conjunto de 
#datos, puede ejecutar el c�digo en el fragmento siguiente:
summarize(diamonds, mean_carat = mean(carat))

```

## Step 4: Visualizing data

#Para crear una visualizaci�n con `ggplot2`, coloque plots de elementos del 
#gr�fico junto con un s�mbolo` + `. 
```{r}
#Este codigo toma los datos de "diamantes", plots la columna de quilates 
#en el eje X, la columna de precio en el eje Y, y representa los datos como un 
#diagrama de dispersi�n usando el comando "geom_point ()".
ggplot(data = diamonds, aes(x = carat, y = price)) +
  geom_point() 
```

 
  ```{r}
#`ggplot2` facilita la modificaci�n o mejora de sus im�genes. Por ejemplo, si 
#desea cambiar el color de cada punto para que represente otra variable, como 
#el corte del diamante, puede cambiar el c�digo de esta manera:
ggplot(data = diamonds, aes(x = carat, y = price, color = cut)) +
  geom_point()
```

```{r}
# A veces, cuando intenta representar muchos aspectos diferentes de sus datos 
#en un objeto visual, puede ser �til separar algunos de los componentes. 
#Por ejemplo, puede crear una parcela diferente para cada tipo de corte. 
#`ggplot2` facilita hacer esto con la funci�n` facet_wrap () `:
ggplot(data = diamonds, aes(x = carat, y = price, color = cut)) +
  geom_point() +
  facet_wrap(~cut)
```

## Step 5: Documentation






