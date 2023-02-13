#_____ Repositorio de ejercicios básicos de Python, uso de CONDICIONALES (if) y CICLOS (while)____


#Calcular el piso convertir un str en un float
inp = input('Europe Floor?')
usf = int(inp) + 1
print('US Floor', usf)

#CALCULAR PAGO con Horas y RATE
xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
xp = float(xh) * float(xr)
print('Pay: ', xp)

#CALCULAR PAGO CON HORAS|condicional simple|

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
if h <= 40:
    pay = h * r
elif h > 40:
    pay = ((h-40)*1.5*r)+(40*r)
print(pay)

#CALCULAR CALIFICACION y corrección de ingreso de texto

from ast import Try
score = input("Enter Score: ")
try:
    fs = float(score)
except:
    print ('Error , debe ingresar un valor numerico')
    quit()
if fs > 1.0 :
    print ('Error of input')
    quit()
else:
    if fs >= 0.9:
        print ('A')
    elif fs >= 0.8:
        print ('B')
    elif fs >= 0.7:
        print ('C')
    elif fs >= 0.6:
        print ('D')
    elif fs < 0.6:
        print ('F')

# CALCULAR EL PAGO DE HORAS y HORAS EXTRA CON FUNCION
def computepay(x, y):
    if x <= 40:
        pay = x * y
    elif x > 40:
        pay = ((x-40)*1.5*y)+(40*y)
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float (hrs)
r = float (rate)

p = computepay(h, r)
print("Pay", p)

#PROGRAMA PARA ORDERAR NÚMEROS Y ARROJAR EL MAYOR Y EL MENOR

largest = None
smallest = None
while True: #inicio Loop
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = int(num)
    except:
        print ('Invalid input') #mensaje de error
        continue
    if smallest is None: #condicional
         smallest = fnum #Guardar el número calculado 
    elif fnum < smallest:
        smallest = fnum
    if largest is None: #condicional
        largest = fnum #Guardar el número calculado 
    elif fnum > largest:
        largest = fnum
    #print(num)
print("Maximum is", largest)
print("Minimum is", smallest)
