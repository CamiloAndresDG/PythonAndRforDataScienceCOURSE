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
 
#TRADUCTOR CON MI IBM CLOUD ACCOUNT
from ibm_watson import LanguajeTranslatorV3
url_lt="https://api.us-south.language-translator.watson.cloud.ibm.com/instances/05d705b1-c060-4b0b-94c1-30ae3fec105b" #Link (Siempre la variable sera url_lt)
apikey_lt="E3b66TrTg8bgCL9OKPgCD8w4g3bwdrcyTJBMIDpt-s3R" #Aqui va el key
version_lt="2018-05-01" #Obtiene la fecha de la version

languaje_translator=LanguajeTranslatorV3(iam_apikey=apikey_lt,url=url_lt,version=version_lt)

languaje_translator.list_identifiable_languajes().get_result() #Se obitene la lista de lenguajes a que se puede traducir
#Por ejemplo Spanish es "es" y ingles "en"

#Ahora para traducirlo
translation_response=languaje_translator.translate(text="Hola, soy Camilo",model_id="es-en") #En este caso va de ingles a español por que el texto esta en ingles
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
    