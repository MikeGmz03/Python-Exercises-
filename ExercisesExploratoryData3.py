# JSON | 


#1. CREA UN jSON E IMPRIME LOS CAMPOS SELECCIONADOS.

import json
#inicia creado de JSON
data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
        } ,
    "email" : {
        "hide" : "yes"
    }
}'''
info = json.loads(data) #carga el JSON con la función loads (Muestra errores de sintaxis zsi existen)
print('Name:', info["name"])
print ('Hide:',info["email"] ["hide"])
#_____________fin de programa________


#2. Funciones adaptables al usar un JSON

import json
datos = '''
[
  { "id" : "001",
    "x" : "2",
    "nombre" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "nombre" : "Brent"
  }
]'''

info = json.loads(datos) #info es una lista
print('Total de usuarios:', len(info)) #podemos determinar cual es su longitud

for elemento in info: # Podemos iterar en la lista
    print('Nombre', elemento['nombre'])
    print('Id', elemento['id'])
    print('Atributo', elemento['x'])

#_____________fin de programa________

#JSON | Explorar datos de JSON y genera un conteo de cada elemento es´pecífico dentro de el (También permite almacenar lños datos específicos de un JSON)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url =  'http://py4e-data.dr-chuck.net/comments_1624322.json'

#url = input ('Enter URL:') #ingresa la URL
#http://py4e-data.dr-chuck.net/comments_42.json url de ejemplo

print ("Retrieving", url)
html = urllib.request.urlopen(url)
data = html.read()

print('Retrieving', url)
print('Retrieved', len(data), 'characters')
info = json.loads(data)
info = info["comments"]
total = 0
for item in info:
    print("Count: ",item["count"])
    total = total + int(item["count"])
    print("Sum: ", total)

print("Final sum: ", total)


