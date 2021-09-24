#Operators
#Es un simbolo que nombra el tipo de operacion o calculo para ser realizado en una fórmula

#Assignment operators
#Usados para asignar valores a variables y vectores
example1 <- c(67.00,50.00,43.00,17.00) #A la variable example1 se le asigna el vector

#Arithmetic operators
#Usados para cumplir calculos matematicos
quater_1<-17.51 #Ventas de la primera mitad del semestre
quater_2<-50.44 #Ventas de la segunda mitad del semestre
midYear<-sale1+sale2 #Obtendremos las sumas de las ventas hasta la mitad de año

year <- midYear * 2 #Obtenemos las ventas durante el año

#Logical Operations
#AND (& o &&)
#OR (| o ||)
#NOT (!)
TRUE & TRUE
TRUE & FALSE
TRUE | TRUE
!TRUE

#&
x <- 10
x > 9 & x <= 10
y <- 7
y > 5 & y < 6

#|
x > 9 | x <= 10
y > 5 | y < 6

#!
!y > 5

#Conditions
#Condition if
if(x > 9){
  print("Vale")
}

#Condition if-else
if(x < 9){
  print("Vale")
}else{
  print("No vale")
}

#Condition if-else
if(x < 9){
  print("Vale")
}else if(x > 5){
  print("OKAY")
}else{
  print("No vale")
}






