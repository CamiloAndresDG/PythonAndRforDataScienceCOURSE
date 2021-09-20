# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:16:36 2021

@author: CamiloDiazG
"""

#HTTP Request
#Cuando usted, el cliente, utiliza una página web, su navegador envía una 
#solicitud HTTP al servidor donde está alojada la página. El servidor intenta 
#encontrar el recurso deseado por defecto "index.html". Si su solicitud tiene 
#éxito, el servidor enviará el objeto al cliente en una respuesta HTTP. #Esto 
#incluye información como el tipo de recurso, la longitud del recurso y 
#otra información.

#Request:
#El proceso se puede dividir en el proceso de solicitud y respuesta. La solicitud 
#que utiliza el método get se ilustra parcialmente a continuación. En la línea 
#de inicio tenemos el método GET, este es un método HTTP. También la ubicación 
#del recurso /index.html y la versión HTTP. El encabezado de solicitud pasa 
#información adicional con una solicitud HTTP:
    
    #METODOS HTTP
    #GET: recupera datos del servidor
    #POST: Sube datos al servidor
    #PUT: Actualiza datos que estan en el servidor
    #DELETE: Borra datos del servidor

#Response:
#La siguiente figura representa la respuesta; la línea de inicio de respuesta 
#contiene el número de versión HTTP / 1.0, un código de estado (200) que 
#significa éxito, seguido de una frase descriptiva (OK). El encabezado de la 
#respuesta contiene información útil. Finalmente, tenemos el cuerpo de respuesta 
#que contiene el archivo solicitado, un documento HTML. Cabe señalar que algunas 
#solicitudes tienen encabezados.

###############################################################################
#Request en Python
import requests
import os 
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)#Tiene información sobre la solicitud, como el estado de la solicitud. 
#Podemos ver el código de estado usando el atributo status_code.
print(r.status_code)
print(r.request.headers) #para ver los headers del request

print("request body:", r.request.body)#Puede ver el cuerpo de la solicitud, en la siguiente línea, ya que no hay cuerpo para una solicitud de obtención, obtenemos None

#Puede ver el encabezado de respuesta HTTP utilizando los encabezados de atributo. Esto devuelve un diccionario de Python de encabezados de respuesta HTTP.
header=r.headers 
print(r.headers)

#Podemos obtener la fecha de envío de la solicitud utilizando la clave Date
header['date']

header['Content-Type']#Contiene el tipo de datos

#Comprobar la codificacion 
r.encoding

#Como el tipo de contenido es text / html, podemos usar el atributo text 
#para mostrar el HTML en el cuerpo. Podemos revisar los primeros 100 caracteres
r.text[0:100]

#Podemos hacer una solicitud de obtención
r=requests.get(url)

#Podemos mirar el encabezado dela respuesta
print(r.headers)
r.headers['Content-Type']


#Puede cargar otros tipos de datos para solicitudes que no sean de texto, 
#como imágenes. Considere la URL de la siguiente imagen
# Use single quotation marks for defining string
url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'


#Una imagen es un objeto de respuesta que contiene la imagen como un objeto de
#tipo bytes. Como resultado, debemos guardarlo usando un objeto de archivo. 
#Primero, especificamos la ruta y el nombre del archivo
path=os.path.join(os.getcwd(),'image.png')
path

#Guardamos el archivo, para acceder al cuerpo de la respuesta usamos el 
#atributo content y luego lo guardamos usando la función open y el método de 
#escritura
with open(path,'wb') as f:
    f.write(r.content)
    
#Podemos ver la imagen
Image.open(path)

####################################
#EJERCICIOS
#En la sección anterior, usamos la función wget para recuperar contenido del 
#servidor web como se muestra a continuación. Escribe el código de Python para 
#realizar la misma tarea. El código debe ser el mismo que se usó para descargar
#la imagen, pero el nombre del archivo debe ser 'Example1.txt'.
#!wget -O /resources/data/Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'example1.txt')
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)


######################################
#GET resquest con parametros URL
#Puede utilizar el método GET para modificar los resultados de su consulta, 
#por ejemplo, recuperar datos de una API. Enviamos una solicitud GET al servidor. 
#Al igual que antes de tener la URL base, en la Ruta que agregamos /get, 
#esto indica que nos gustaría realizar una solicitud GET. Esto se demuestra en 
#la siguiente tabla

#La URL base es para http://httpbin.org/ es un simple servicio de solicitud y 
#respuesta HTTP. La URL en Python viene dada por:
url_get='http://httpbin.org/get'

#Para crear una cadena de consulta, agregue un diccionario. Las claves son los 
#nombres de los parámetros y los valores son el valor de la cadena de consulta.
payload={"name":"Joseph","ID":"123"}

#Luego, pasando la carga útil del diccionario al parámetro params de la función
#get():
r=requests.get(url_get,params=payload)

#Podemos imprimir el URL y ver los nombres y valores
r.url

#No hay request body
print("request body:", r.request.body)

#Podemos imprimir el estado del codigo
print(r.status_code)

#Podemos ver la respuesta como texto
print(r.text)

#Podemos ver el tipo del contenido 
r.headers['Content-Type'] #Esto retornara un JSON podemos pasarlo a diccionario

r.json() #De esta manera se exporta el JSON a Diccionario

#La key args tiene el nmobre y los valores
r.json()['args']

###############################################
#POST request
#Al igual que una solicitud GET, una POST se usa para enviar datos a un 
#servidor, pero la solicitud POST envía los datos en un cuerpo de solicitud. 
#Para enviar la Solicitud de Publicación en Python, en la URL cambiamos la 
#ruta a POST
url_post='http://httpbin.org/post'

#This endpoint will expect data as a file or as a form. A form is convenient 
#way to configure an HTTP request to send data to a server.
#o make a POST request we use the post() function, the variable payload is 
#passed to the parameter  data
r_post=requests.post(url_post,data=payload)

#Al comparar la URL del objeto de respuesta de la solicitud GET y POST, 
#vemos que la solicitud POST no tiene pares de nombre o valor.
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)

#Podemos comparar el cuerpo de la solicitud POST y GET, vemos que solo la 
#solicitud POST tiene un cuerpo
print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

#Podemos ver the form tambien
r_post.json()['form']
