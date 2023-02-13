#Programa que muestra la sucesión de fibonacci con una cantidad específica de números determinado por el número ingresado | test de HackerRank

def fibonacci(n): #Define la función
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2]) #construccion de la sucesión cuando es diferente a casos especiales 1 y 2.
        return fib

number = int(input("Ingrese la cantidad de números que desea ver en la sucesión de Fibonacci: "))
print(fibonacci(number))
