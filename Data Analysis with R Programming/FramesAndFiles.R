#Data FRAMES Los frames de datos son la forma más común de almacenar y analizar 
#datos en R, por lo que es importante comprender qué son y cómo crearlos. 
#Un frame de datos es una colección de columnas, similar a una hoja de cálculo o 
#una tabla SQL.
data.frame(x = c(1, 2, 3) , y = c(1.5, 5.5, 7.5))

#MATRICES
#A matrix is a two-dimensional collection of data elements. This means it has both rows and columns. 
#But like vectors, matrices can only contain a single data type.
matrix(c(3:8), nrow = 2) #Primer argumento matriz y segundo es el numero de filas
matrix(c(3:8), ncol = 2) #Tambien se puede el numero de columnas

#FILES
dir.create("CarpetaFILES_RCourse") #Si se crea retornara TRUE de lo contrario FALSE

file.create ("new_text_file.txt") #Si se crea retornara TRUE de lo contrario FALSE
file.create ("new_word_file.docx") #Si se crea retornara TRUE de lo contrario FALSE 
file.create ("new_csv_file.csv") #Si se crea retornara TRUE de lo contrario FALSE

file.copy ("new_text_file.txt" , "CarpetaFILES_RCourse") #Para copiar un archivo el primer argumento es el archivo y el segundo es la carpeta destino

unlink ("some_.file.csv") #Como no existe retornara un FALSE




