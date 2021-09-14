install.packages('palmerpenguins')
library('palmerpenguins')

install.packages('ggplot2')
library('ggplot2')

ggplot(data=penguins,aes(x=flipper_length_mm, y=body_mass_g))+geom_point()

##Para hacer un resumen
summary(penguins)

##Para mostrar los datos en tabla
View(penguins)

##Para agregar colores a los puntos
ggplot(data=penguins,aes(x=flipper_length_mm, y=body_mass_g))+geom_point(color="green")

##Para cambiar los colores de los puntos dependiendo de la especie
ggplot(data=penguins,aes(x=flipper_length_mm, y=body_mass_g))+geom_point(aes(color=species))

##Para cambiar en ves de circulos a figuras por especie
ggplot(data=penguins,aes(x=flipper_length_mm, y=body_mass_g))+geom_point(aes(shape=species))

##Para cambiar los colores de las figuras por especie
ggplot(data=penguins,aes(x=flipper_length_mm, y=body_mass_g))+geom_point(aes(shape=species,color=species))

##Para agrupar por especie
ggplot(data=penguins,aes(x=flipper_length_mm, y=body_mass_g))+geom_point(aes(shape=species,color=species))+facet_wrap(~species)

##Para poner titulo
ggplot(data=penguins,aes(x=flipper_length_mm, y=body_mass_g))+geom_point(aes(shape=species,color=species))+facet_wrap(~species)+labs(title = 'Palmer penguin: Body Mass vs. Flipper Lenght')

##Instalacion de Tidyverse
install.packages("tidyverse")

##Carga de la libreria (Siempre se tiene que hacer)
library(tidyverse)

##Carga de la libreria (Lubridate)
library(lubridate)