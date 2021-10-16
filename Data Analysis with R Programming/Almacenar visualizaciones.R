library(ggplot2)
library(palmerpenguins)

ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color=species))
#Al reproducir esto, podemos almacenar en la parte de la grafica la opcion de save image

#Tambien lo podemos almacenar con la funcion ggsave()
ggsave("Three Penguin Species.png")#Si lo ejecutamos almacenara el ultimo plot con ese nombre y tipo de archivo