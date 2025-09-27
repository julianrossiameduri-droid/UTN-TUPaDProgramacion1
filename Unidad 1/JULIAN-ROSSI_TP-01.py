#1. 

def holamundo():

    print("Hola Mundo!")

#2. 

def saludo_nombre():

    nombre = input("¿Cual es tu nombre?" )
    print(f"Hola {nombre}!")

#3. 

def detalle_usuario():

    nombre = input("¿Cual es tu nombre?" )
    apellido = input("¿Cual es tu apellido?" )
    edad = input("¿Cual es tu edad?" )
    lugar_residencia = input("¿Cual es tu lugar de residencia?" )

    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

#4. 

def radio_circulo():

    radio = int(input("Ingrese radio de un circulo: "))
    area = 3.14 * radio ** 2
    perimetro = 2 * 3.14 * radio
    
    print(f"El area es de {area} y el perimetro es de {perimetro}")

#5. 

def segundos_a_horas():

    segundos = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos / 3600
    print(f"{segundos} segundos equivalen a {horas} horas")

#6. 

def tabla_multiplicar():

    numero = int(input("Ingrese un número: "))
    print(f"Tabla de multiplicar del {numero}:")
    print(f"{numero} x 1 = {numero * 1}")
    print(f"{numero} x 2 = {numero * 2}")
    print(f"{numero} x 3 = {numero * 3}")
    print(f"{numero} x 4 = {numero * 4}")
    print(f"{numero} x 5 = {numero * 5}")
    print(f"{numero} x 6 = {numero * 6}")
    print(f"{numero} x 7 = {numero * 7}")
    print(f"{numero} x 8 = {numero * 8}")
    print(f"{numero} x 9 = {numero * 9}")
    print(f"{numero} x 10 = {numero * 10}")

#7. 

def operaciones():

    num1 = int(input("Ingrese el primer número (distinto de 0): "))
    num2 = int(input("Ingrese el segundo número (distinto de 0): "))

    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    print(f"División: {num1 / num2}")

#8. 

def calcular_imc():

    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    imc = peso / (altura ** 2)

    print(f"Su IMC es: {imc}")

#9.

def celsius_a_fahrenheit():

    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (9/5) * celsius + 32
    print(f"{celsius}°C equivalen a {fahrenheit}°F")

#10.

def calcular_promedio():

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    
    promedio = (num1 + num2 + num3) / 3
    print("El promedio de los tres números es:", promedio)
