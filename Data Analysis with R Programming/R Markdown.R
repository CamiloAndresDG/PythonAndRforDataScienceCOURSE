#R Markdown
  #Es un formato de documento para hacer documentos dinamicos en R

#Markdown
  #Es una sintaxis para formatear archivos de texto sin formato
install.packages("rmarkdown")

#Para crear un archivo R Markdown se tiene que ir a crear nuevo archivo ->R Markdown
#Para visualizar el archivo creado se da click en knit

#ESTE ES UN EJEMPLO, AQUI NO FUNCIONA POR QUE NO ES EL TIPO DE ARCHIVO 

#Esto es una YAML
  #YAML es un lenguaje para datos que lo traduce leible.
---
  title: "R Markdown Introdution"
author: "Camilo"
date: "10/15/2021"
output: html_document
---
  
  ```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

## R Markdown

This is an R Markdown document. Markdown is a simple formatting syntax for authoring HTML, PDF, and MS Word documents. For more details on using R Markdown see <http://rmarkdown.rstudio.com>.

When you click the **Knit** button a document will be generated that includes both content as well as the output of any embedded R code chunks within the document. You can embed an R code chunk like this:
  
  ```{r cars}
summary(cars)
```

## Including Plots

You can also embed plots, for example:
  
  ```{r pressure, echo=FALSE}
plot(pressure)
```

Note that the `echo = FALSE` parameter was added to the code chunk to prevent printing of the R code that generated the plot.
