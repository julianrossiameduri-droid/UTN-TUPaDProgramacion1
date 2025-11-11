
"""
Programación I - TP: Funciones
Todas las funciones definidas de manera separada, sin ejecución ni ejemplos.
"""

import math

# Ejercicio 1
def imprimir_hola_mundo() -> None:
    """Imprime el mensaje 'Hola Mundo!'."""
    print("Hola Mundo!")

# Ejercicio 2
def saludar_usuario(nombre: str) -> str:
    """Devuelve un saludo personalizado para el nombre dado."""
    return f"Hola {nombre}!"

# Ejercicio 3
def informacion_personal(nombre: str, apellido: str, edad: int, residencia: str) -> None:
    """Imprime una línea con la información personal formateada."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4
def calcular_area_circulo(radio: float) -> float:
    """Devuelve el área de un círculo a partir de su radio."""
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio: float) -> float:
    """Devuelve el perímetro (circunferencia) de un círculo a partir de su radio."""
    return 2 * math.pi * radio

# Ejercicio 5
def segundos_a_horas(segundos: int) -> float:
    """Convierte una cantidad de segundos a horas."""
    return segundos / 3600.0

# Ejercicio 6
def tabla_multiplicar(numero: int) -> list[str]:
    """Devuelve una lista con la tabla de multiplicar del número del 1 al 10."""
    return [f"{numero} x {i} = {numero * i}" for i in range(1, 11)]

# Ejercicio 7
def operaciones_basicas(a: float, b: float) -> tuple[float, float, float, float | None]:
    """Devuelve una tupla con (suma, resta, multiplicación, división)."""
    suma = a + b
    resta = a - b
    multi = a * b
    division = a / b if b != 0 else None
    return (suma, resta, multi, division)

# Ejercicio 8
def calcular_imc(peso: float, altura: float) -> float:
    """Devuelve el índice de masa corporal (IMC)."""
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que cero.")
    return peso / (altura ** 2)

# Ejercicio 9
def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    return celsius * 9/5 + 32

# Ejercicio 10
def calcular_promedio(a: float, b: float, c: float) -> float:
    """Devuelve el promedio de tres números."""
    return (a + b + c) / 3
