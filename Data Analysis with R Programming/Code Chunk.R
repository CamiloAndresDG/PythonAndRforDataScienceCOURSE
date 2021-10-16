#CODE CHUNK
  #Es codigo agregado a un archivo .RMD

library(ggplot2)
library(palmerpenguins)

ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g)) 
#El unico problema es que no podemos saber a que raza de pinguinos se refiere

ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color=species))
#Ahora muestra a que se especie hace referencia cada punto con colores

ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,shape=species))
#Ahora muestra a que se especie hace referencia cada punto con figuras

ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,shape=species,color=species))
#Ahora muestra a que se especie hace referencia cada punto con figuras y colores

ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,shape=species,color=species,size=species))
#Ahora muestra a que se especie hace referencia cada punto con figuras y colores y diferentes tamaños

ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g),color="purple")
#Ahora muestra las especies con un color preseleccionado

ggplot(data=penguins)+
  geom_smooth(mapping = aes(x=flipper_length_mm,y=body_mass_g),color="purple")
#Ahora muestra la grafica pero en linea

ggplot(data=penguins)+
  geom_smooth(mapping = aes(x=flipper_length_mm,y=body_mass_g),color="purple")+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g)) 
#combina grafica de linea con puntos

ggplot(data=penguins)+
  geom_smooth(mapping = aes(x=flipper_length_mm,y=body_mass_g,linetype=species),color="purple")
#Ahora muestra la grafica pero en linea por cada raza de pinguino

ggplot(data=penguins)+
  geom_jitter(mapping = aes(x=flipper_length_mm,y=body_mass_g,linetype=species),color="purple")
#Con geom_jitter

#AHORA CON DIMONDS
ggplot(data=diamonds)+
  geom_bar(mapping=aes(x=cut))
#Ahora muestra en grafico de barras

ggplot(data=diamonds)+
  geom_bar(mapping=aes(x=cut,color=cut))
#Ahora muestra en grafico de barras con diferentes colores por fuera

ggplot(data=diamonds)+
  geom_bar(mapping=aes(x=cut,fill=cut))
#Ahora muestra en grafico de barras con diferentes colores por dentro

ggplot(data=diamonds)+
  geom_bar(mapping=aes(x=cut,fill=clarity))
#Con otro valor de la tabla, teniendo en cuenta el corte

#+FACET_WRAP
ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,shape=species,color=species))+
  facet_wrap(~species)
#Se divide por especies

ggplot(data=diamonds)+
  geom_bar(mapping = aes(x=color,fill=cut))+
  facet_wrap(~cut)
#se divido por color y corte

ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color=species))+
  facet_wrap(sex~species)
#Se divide por sexo

ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color=species))+
  facet_wrap(~sex)

