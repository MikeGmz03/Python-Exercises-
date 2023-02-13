#DICTIONARIES | de un archivo, buscar las lineas del remitente 'From', luego tomar el nombre del remitente

# Contar cuantes veces se repite el remitente y mostrar el nombre del mas repetido y la cantidad de veces

fname = input("Enter file name: ") #IMPORTA EL ARCHIVO DE TEXTO
if len(fname) < 1: 
    fname = "mbox-short.txt" #esto es para no tener que agregar la palabra del archivo, usar mbox-short.txt por defecto
fh = open(fname)

#INICIA EL RECORRIDO DEL ARCHIVO Y FILTRADO DE LAS LINEAS A INTERES
lista=list()
for line in fh: 
    line= line.rstrip() #dividir el texto en frases
    if not line.startswith('From '):
        continue
    words = line.split() #dividir las frases en palabras separadas por espacios
    lista.append(words[1]) # aca se guarda en la lista solo las palabras que contienen el nombre del remitente


#print(lista) \\\ print para probar que la lsita tenga los datos que nos interesan/////
# hasta aca, se saca listado de los remitentes

#Empieza codigo que convierte el listado en un diccionario de frecuencia absoluta (cuantas veces se repite)
counts = dict()
for x in lista: # se hace el llamado de la lista y se recorre en x (cada elemento)
    counts [x] = counts.get(x,0) + 1
#se almacena en diccionario counts

#inicia funcion para seleccionar el mayor
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount) #imprime el mayor y su frecuencia absoluta.


#_____________fin de programa________

#DICTIONARIES | buscar las palabras mas repetidas en el archivo y mostrar la palabra y cuantas veces se repite

name = input('Enter file:')
handle=open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts [word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)

#_____________fin de programa________


#<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>

# FILES| Ingrese nombre del archivo e imprima su contenido en letra mayuscula sostenida y sin líneas de espacios

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip() #cadena.rstrip() para quitar espacios entre líneas
    print(line.upper()) #cadena. upper() para convertir en myúsculas

#FILES | Extraer línea, convertir número, contar líneas y promedio.
fname = input("Enter file name: ")
fh = open(fname)
count= 0
snumb=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # print(line) 
    count = count +1
    numb = float(line[20:]) #busca desde la posición 20 hasta el final [20:]
    #print(numb)
    snumb = snumb + numb

average = snumb / count 
#print (count)
#print (snumb)
#print (average)
print("Average spam confidence: ", average)
#_____________fin de programa________

#<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>

#LISTS| leer documento, dividirlo en líneas, dividir las líneas en palabras y organizarlas en una lista en orden alfabético 
# (Eliminando palabras repetidas)
fname = 'romeo.txt'
#fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh: #divide el texto en líneas
    words = line.rstrip().split() #separa las líneas en listas de palabras y a su vez la lista de palabras en palabras sueltas
    for w in words: #para cada elemento de las palabras
        if w in lst: #Si el elemento ya está en la lista (false)
            continue  #salte a la siguiente palabra
        else: #si no está el elemento en la lista
            lst.append(w) #agrege el elemento a la lista
lst.sort() #acomode la lista en orden alfabético
print(lst) #imprima la lista
#_____________fin de programa________


#LISTS| leer documento, dividirlo en líneas, dividir las líoneas en palabras y organizarlas en una lista en orden alfabético 
# (Eliminando palabras repetidas)
# ----------------Segunda manera de hacer el ejercicio--------------------
#fname = input("Enter file name: ")
fname='romeo.txt'
fh = open(fname)
lst = list()
for line in fh: #divide el texto en líneas
    words = line.split() #separa las líneas en listas de palabras
    for word in words: #para cada palabra en la lista de palabras
        if word not in lst: #condicional: si la palabra no esta en lña lista
            lst.append(word) #agrega la palabra  ala lista
lst.sort()
print(lst) 

#_____________fin de programa________

#LISTS |  Ejercicio 2, imprimir los correos de los remitentes e indicar cuantos remitentes hay 

fname = input("Enter file name: ")
if len(fname) < 1: 
    fname = "mbox-short.txt" #esto es para no tener que agregar la palabra del archivo, usar mbox-short.txt por defecto
fh = open(fname)
#
count = 0
for line in fh:
    line= line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    count = count +1
    print(words[1]) 
print("There were", count, "lines in the file with From as the first word")
#_____________fin de programa________

#<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>
#Strings | encontrar un número y convertirlo a float - imprimirlo

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(' ')
num=(text[pos:pos+100])
fnum = float(num)
print (fnum)
#_____________fin de programa________


