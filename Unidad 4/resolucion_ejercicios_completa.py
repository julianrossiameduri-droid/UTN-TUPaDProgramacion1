# Resolución de ejercicios - Python

# Ejercicio 1
for i in range(0, 101):
    print(i)

print("-----")

# Ejercicio 2
n = int(input("Ingrese un número entero: "))
n_abs = abs(n)
if n_abs == 0:
    digitos = 1
else:
    digitos = 0
    while n_abs > 0:
        n_abs //= 10
        digitos += 1
print("Cantidad de dígitos:", digitos)

print("-----")

# Ejercicio 3
a = int(input("Ingrese primer valor: "))
b = int(input("Ingrese segundo valor: "))
if a > b:
    a, b = b, a
suma = 0
for i in range(a+1, b):
    suma += i
print("Suma (excluyendo extremos):", suma)

print("-----")

# Ejercicio 4
total = 0
while True:
    n = int(input("Ingrese número (0 para terminar): "))
    if n == 0:
        break
    total += n
print("Total acumulado:", total)

print("-----")

# Ejercicio 5
import random
objetivo = random.randint(0,9)
intentos = 0
while True:
    guess = int(input("Adivine el número (0-9): "))
    intentos += 1
    if guess == objetivo:
        break
print("Adivinaste en", intentos, "intentos.")

print("-----")

# Ejercicio 6
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

print("-----")

# Ejercicio 7
n = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(0, n+1):
    suma += i
print("Suma:", suma)

print("-----")

# Ejercicio 8
pares = 0
impares = 0
positivos = 0
negativos = 0
cantidad = 100 # cambiar para probar si se quiere
for i in range(cantidad):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num >= 0:
        positivos += 1
    else:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

print("-----")

# Ejercicio 9
cantidad = 100 # cambiar para probar si se quiere
suma = 0
for i in range(cantidad):
    num = int(input("Ingrese un número: "))
    suma += num
print("Media:", suma / cantidad)

print("-----")

# Ejercicio 10
num = int(input("Ingrese un número: "))
invertido = 0
while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num //= 10
print("Invertido:", invertido)
