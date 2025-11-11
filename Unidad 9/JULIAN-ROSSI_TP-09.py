# ------------------------------------------------------------
# TP 9: Aplicación de la Recursividad
# Materia: Programación I
# Tecnicatura Universitaria en Programación
# ------------------------------------------------------------
# Objetivo:
# Comprender el uso de la recursividad en problemas matemáticos simples.
# ------------------------------------------------------------

# EJERCICIO 1

def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)

# EJERCICIO 2

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# EJERCICIO 3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# EJERCICIO 4

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
# EJERCICIO 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# EJERCICIO 6

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# EJERCICIO 7

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# EJERCICIO 8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        contador = 1 if numero % 10 == digito else 0
        return contador + contar_digito(numero // 10, digito)