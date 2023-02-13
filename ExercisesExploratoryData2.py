#REGULAR EXPRESIONS | find(), re.search(), startswith(), re.findall()


# buscar usando find() e imprimir la línea completa
hand = open ('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:')>= 0:
        print(line)
#_____________fin de programa________

# MISMO CÓDIGO ANTERIOR, pero usando  re.search()
import re
hand = open ('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
#_____________fin de programa________

#-- mismo programa usando startswith()
hand = open ('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
#_____________fin de programa________

#-- usando re.search()
import re
hand = open ('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line): #se le agrega el prefijo ^ 
        print(line)
#_____________fin de programa________
        
# usando re.findall() para encontrar valores uméricos y extraerlos con la llave [0-9]+ 
import re
x= 'My 2 favorite numbers are 19 and 42'
y=re.findall('[0-9]+',x)
print(y)# devuelvoe la lista ['2', '19', '42']
#_____________fin de programa________

#Buscar y Extraer datos
import re
x= 'My 2 favorite numbers are 19 and 42'
y=re.findall('[0-9]+',x)
#_____________fin de programa________

#-----Método no codicioso (non-greedy) de la busqueda
import re
x = 'From: Using the : character'
y =re.findall('F.+?:', x)
print (y)
#Imprime ['From:']
#_____________fin de programa________

#---Método codicioso (greedy) de la busqueda---
import re
x = 'From: Using the : character'
y =re.findall('F.+:', x)
print (y)
#Imprime ['From: Using the :']
#_____________fin de programa________

#-- Encontrar contenido entre espacios
y= re.findall('\s+@\s+', x)
print(y)

#--encontrar contenido entre espacios luego de un From:

y= re.findall('^From (\s+@\s+)', x)
print(y)

#---- SPAM CONFIDENCE (Buscar remitente y filtrarlo)

import re
hand = open ('mbox-short.txt')
numlist = list()
for line in hand:
    line=line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len (stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print ('Maximum: ', max(numlist))
#_____________fin de programa________

#--- extraer el valor numérico pero integrando el símbolo '$'
import re
x= 'We just received $10.00 for cookies '
y= re.findall ('\$[0-9.]+', x)
print (y)
#imprime >>['$10.00']
#_____________fin de programa________
#<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>



