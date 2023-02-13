#NETWORKED | exploración de datos en HTTP, exploración de datos de páginas web (No uso de BeautifulSoup)



#HTTP | Request in python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len (data) < 1):
        break
    print (data.decode())
mysock.close()
#_____________fin de programa________


# Decode | Strings to Bytes
while True :
    data = mysock.recv(512)
    if ( len ( data ) < 1 ) :
        break
    mystring = data.decode ( )
    print ( mystring )
#_____________fin de programa________

#Encode y Decode text | Criptografía de datos
import socket
mysock = socket.socket (socket.AF_INET , socket . SOCK_STREAM )
mysock.connect ( ( ' data.pr4e.org ' , 80 ) )
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP /1.0\n\n'.encode ( )
mysock.send(cmd)
while True:
    data = mysock.recv ( 512 )
    if (len(data)<1):
        break
    print (data.decode())
mysock.close()
#_____________fin de programa________

#Using urllinb in Python
import urllib.request , urllib.parse , urllib.error
fhand = urllib.request.urlopen ('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print (line.decode( ).strip())  
#_____________fin de programa________

#URL | Usar una URL como un archivo para exploprar sus datos
# Contar las palabras en un archivo de texto de sitio web

import urllib.request , urllib.parse , urllib.error
fhand = urllib.request.urlopen ( ' http://data.pr4e.org/romeo.txt ' )
counts = dict ( )
for line in fhand:
    words = line.decode ( ) . split ( )
    for word in words:
        counts [ word] = counts.get ( word , 0 ) + 1
print(counts)
#_____________fin de programa________

#URL | Leer páginas web
#--> genera un listado de atributos de la página web
import urllib.request , urllib.parse , urllib.error
fhand = urllib.request.urlopen ( 'http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print (line.decode().strip())
#_____________fin de programa________
    

#URL | Permite la suma de los números de la URL (Toma una página web como archivo de texto)
#programa que permite la suma de los números de la URL
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url: http://py4e-data.dr-chuck.net/comments_1624319.html Url de ejemplo
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

spans = soup('span')
numbers = []

for span in spans:
    numbers.append(int(span.string))

print (sum(numbers))
#_____________fin de programa________


#URL | Programa que segun el numero ingresado cuenta las líneas de un contenido web y repite tantas veces lo indique | USO DE BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#URL http://py4e-data.dr-chuck.net/known_by_Ophelia.html

url = input('Enter - ')
count = int(input("Enter count: "))
position = int(input("Enter position: "))


names = []

while count > 0:
    print ("retrieving: {0}".format(url))
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup('a')
    name = anchors[position-1].string
    names.append(name)
    url = anchors[position-1]['href']
    count -= 1

print (names[-1])
#_____________fin de programa________

