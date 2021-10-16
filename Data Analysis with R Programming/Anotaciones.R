library(ggplot2)
library(palmerpenguins)

#Para agregar titulos
ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color=species))+
  labs(title="Palmer penguins: Body Mass vs Flipper Lenght")

#Para agregar subtitulos
ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color=species))+
  labs(title="Palmer penguins: Body Mass vs Flipper Lenght",subtitle = "Sample of Three Penguin Species")

#Para agregar una nota en la parte inferior
ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color=species))+
  labs(title="Palmer penguins: Body Mass vs Flipper Lenght",subtitle = "Sample of Three Penguin Species",
       caption = "Data colleted by Dr. Kristen Gorman")

#Agregar anotaciones
ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color=species))+
  labs(title="Palmer penguins: Body Mass vs Flipper Lenght",subtitle = "Sample of Three Penguin Species",
       caption = "Data colleted by Dr. Kristen Gorman")+
  annotate("text",x=200,y=3500,label="The Gentoos are the largest")

#Agregar anotaciones con diferente color
ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color=species))+
  labs(title="Palmer penguins: Body Mass vs Flipper Lenght",subtitle = "Sample of Three Penguin Species",
       caption = "Data colleted by Dr. Kristen Gorman")+
  annotate("text",x=200,y=3500,label="The Gentoos are the largest",
           color="red")

#Agregar anotaciones con negrilla, diferente tamaño y angulo
ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color=species))+
  labs(title="Palmer penguins: Body Mass vs Flipper Lenght",subtitle = "Sample of Three Penguin Species",
       caption = "Data colleted by Dr. Kristen Gorman")+
  annotate("text",x=200,y=3500,label="The Gentoos are the largest",
           color="red",
           fontface="bold",
           size=4.5,
           angle=25)

#Ahora si queremos almacenar el plot en una variable
p<-ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color=species))+
  labs(title="Palmer penguins: Body Mass vs Flipper Lenght",subtitle = "Sample of Three Penguin Species",
       caption = "Data colleted by Dr. Kristen Gorman")

#Ahora si a la variable queremos agregarle una anotacion
p+annotate("text",x=200,y=3500,label="The Gentoos are the largest",
           color="red")
