# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 00:30:59 2021

@author: CamiloDiazG
"""
range(5) #Da una lista de numeros de 0 a 5
print(range(5))

#For lops
squares=["red","blue","white","green","blue"] #Hay 5 atributos por lo tanto su tamanio es 5

for i in range(0,5):#Tambien se puede agregando 0,len(squares)
    squares[i]="white"
#Tambien se puede recorer
for square in squares:
    print(square) #Se obtiene solo el valor
print("---")
#Otra manera para recorrerlo con valor e indice
for i, square in enumerate(squares):
    print(i, square)
    
squares3 = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square ", i, 'is',  squares3[i])
    squares3[i] = 'white'
    print("After square ", i, 'is',  squares3[i])    

# Print the elements of the following list: Genres
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for gen in Genres:
    print(gen)


#LABS
#Use loops to print out the elements in the list A
A=[3,4,5]
for i in range(0,3):
    print(A[i])
for i in A:
    print(i)

# For loop example with dates
dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])     

for year in dates:  
    print(year)   

#While lops
squares2=["Orange","Orange","Purple","Blue"]
squaresCopy=[]
i=0
while(squares2[i]=="Orange"):
    squaresCopy.append(squares2[i])
    i=i+1
print(squaresCopy)

#LAB
#Write a while loop to display the values of the Rating of an album
#playlist stored in the list PlayListRatings. If the score is less than 6,
#exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]
while(i < len(PlayListRatings) and Rating >= 6):
    Rating = PlayListRatings[i]
    print(Rating)
    i = i + 1
    
#Write a while loop to copy the strings 'orange' of the list squares to the 
#list new_squares. Stop and exit the loop if the value on the list is not 
#'orange':
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)