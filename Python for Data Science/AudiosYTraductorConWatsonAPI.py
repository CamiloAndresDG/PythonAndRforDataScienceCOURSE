# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 08:09:42 2021

@author: CamiloDiazG
"""

#Pasar un audio a texto usando Watson Text to Speech API
#Traducir el texto a otro idioma

#Los APIs Keys y los endpoints nos daran acceso al API
#Los APIs Keys son un medio de acceso al API. 
 #Es un unico set de caracteres que el API usa para identificarme y autorizarme
 #SE TIENE QUE TENER EL API Key DE FORMA SECRETA
 
from ibm_watson import SpeechToTextV1
url_s2t= "https://stream.watsonplatform.net/speech-to-text/api" #Link (Siempre la variable sera url_s2t)
st2="Exx377GHD8nXn" #Aqui va el key

filename="AudioAConvertir.wav" #Archivo a convertir
with open(filename,mode="rb") as wav: #El rb siginica que leera el archivo de forma binaria
    #recognize es el metodo del API
    response=st2.recognize(audio=wav,content_type="audio/wav")
    
    #La variable response almanecera un diccionario 
    #En esta se encontrara un key=transcript el cual contendra el texto
    #Este texto lo podemos asignar a otra variable
    recognized_text=response.results["results"][0]["alternatives"][0]["transcript"] #Aqui estara el String del texto (VER WHATSAPP)

#TRADUCTOR
from ibm_watson import LanguajeTranslatorV3
url_lt="https://gateway.watsonplatform.net/languaje-translator/api" #Link (Siempre la variable sera url_lt)
apikey_lt="EIC898XXNFM33ndbb34CC" #Aqui va el key
version_lt="2018-05-01" #Obtiene la fecha de la version

languaje_translator=LanguajeTranslatorV3(iam_apikey=apikey_lt,url=url_lt,version=version_lt)

languaje_translator.list_identifiable_languajes().get_result() #Se obitene la lista de lenguajes a que se puede traducir
#Por ejemplo Spanish es "es" y ingles "en"

#Ahora para traducirlo
translation_response=languaje_translator.translate(text=recognized_text,model_id="en-es") #En este caso va de ingles a español por que el texto esta en ingles
translation=translation_response.get_result() #Obtiene la traduccion el cual estara en un diccionario

spanish_translation=translation["translations"][0]["translation"] #Se obtiene del diccionario la traduccion (VER WHATSAPP)
print(spanish_translation)

#Tambien podemos volver el texto traducido a ingles
translation_new=languaje_translator.translate(text=spanish_translation,model_id="es-en").get_result() #Esto devolvera el texto anterior traducido a ingles en un diccionario
translation_eng=translation_new["translations"][0]["translation"]
print(translation_eng)

#EJEMPLO DE TRADUCIR DE INGLES A FRANCES
french_translation=languaje_translator.translate(text=translation_eng,model_id="en-fr").get_result() #Esto devolvera el texto anterior traducido a frances en un diccionario
translation_french=french_translation["translations"][0]["translation"]
print(translation_french)
    