id <- c(1:10)

name <- c("John Mendes", "Rob Stewart", "Rachel Abrahamson", "Christy Hickman", "Johnson Harper", "Candace Miller", "Carlson Landy", "Pansy Jordan", "Darius Berry", "Claudia Garcia")

job_title <- c("Professional", "Programmer", "Management", "Clerical", "Developer", "Programmer", "Management", "Clerical", "Developer", "Programmer")

employee <- data.frame(id, name, job_title)

print(employee)

#FUncion separate
separados<-separate(employee,name,into=c('first_name','last_name'),sep=' ')
 #Con esta funcion se puede separar en varias columnas una columna

#Funcion unate
unite(separados,'name',first_name,last_name,sep=' ')
 #COn esta funcion podemos juntar dos columna separadas


#Funcion mutate
#COn esta funcion se pueden crear nuevas columnas
#con datos aritmeticos

View(penguins)

penguins %>% 
mutate(body_mass_kg=body_mass_g/1000) 
 #Se creo una nueva columna llamada body_mass_kg
 #en donde agrego los kilogramos obtenidos por la division
 #entre body_mass_g/1000

#Tambien podemos crear mas columnas con la misma funcion

penguins %>% 
  mutate(body_mass_kg=body_mass_g/1000,flipper_length_m=flipper_length_mm/1000)
#Se creo una nueva columna llamada body_mass_kg
#en donde agrego los kilogramos obtenidos por la division
#entre body_mass_g/1000
#Tambien se crea una nueva columna con nombre flipper_length_m
#donde se agregara los datos obtenidos de flipper_length_mm en metros
