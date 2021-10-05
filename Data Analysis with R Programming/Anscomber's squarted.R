#Anscomber's squarted
install.packages("Tmisc")
library(Tmisc)
data(quartet)
View(quartet)

quartet %>% 
  group_by(set) %>% 
  summarize(mean(x),sd(x),mean(y),sd(y),cor(x,y)) #Se obtienen los summary
  #Por cada columna

ggplot(quartet,aes(x,y))+geon_point()+geom_smooth(method=lm,se=FALSE)+facet_wrap(~set)

install.packages("datasauRus")
library("datasauRus")

ggplot(datasaurus_dozen,aes(x=x,y=y,colour=dataset))+geom_point()+theme_void()+theme(legend.position="none")