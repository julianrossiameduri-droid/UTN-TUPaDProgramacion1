#1. 

def validar_edad():

    edad = int(input("¿Cual es tu edad?: "))

    if edad >= 18:
        print("Eres mayor de edad")

#2. 

def aprobado_nota():

    nota = int(input("¿Cual es tu nota?: "))

    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

#3.

def validacion_pares():

    numero = int(input("Ingrese un numero: "))

    if numero % 2 == 0:
        print("Ha ingresado un numero par")
    else:
        print("Por favor, ingrese un numero par") 

#4.

def edad_categoria():

    edadcat = int(input("¿Cual es tu edad?: "))

    if edadcat < 12:
        print("Niño/a")
    elif edadcat >= 12 and edadcat < 18:
        print("Adolescente")
    elif edadcat >= 18 and edadcat < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

#5. 

def caracteres_contraseñas():

    password = input("Escriba su contraseña: ")

    if len(password) >= 8 and len(password) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6. 

def statics():

    from statistics import mode, median, mean

    import random
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    
    valor_mode = mode(numeros_aleatorios)   
    valor_median = median(numeros_aleatorios)   
    valor_mean = mean(numeros_aleatorios) 

    print(f"Moda: {valor_mode}, Mediana: {valor_median}, Media: {valor_mean}")  

    if valor_mode == valor_median == valor_mean:
        print("Sin sesgo")
    elif valor_mean < valor_median and valor_median < valor_mode:
        print("Sesgo negativo o a la izquierda")
    elif valor_mean > valor_median and valor_median > valor_mode:
        print("Sesgo positivo o a la derecha")

#7.

def validar_frase():

    frase = input("Escriba una frase o palabra: ")
    vocales = "aeiouAEIOU"

    if frase[len(frase) - 1] in vocales:
        frase = frase + "!" 
        print(frase)
    else:
        print(frase)

validar_frase()

#8.

def modif_name():

    nombre = input("¿Cual es tu nombre?: ")
    valorcase = int(input("Ingrese un numero del uno al tres: "))

    if valorcase == 1:
        print(nombre.upper())
    elif valorcase == 2:
        print(nombre.lower())
    elif valorcase == 3:
        print(nombre.title())
    else:
        print("El valor numerico ingresado, no es valido.")

#9.

def validar_terremoto():

    magnitud = float(input("Ingrese la magnitud del terremoto: "))

    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif magnitud >= 3 and magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif magnitud >= 4 and magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif magnitud >= 5 and magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif magnitud >= 6 and magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")

#10.

def estacion_del_anio():

    hemisferio = input("¿En que hemisferio estas? (N/S): ")
    mes = int(input("Ingrese el mes (1-12): "))
    dia = int(input("Ingrese el día (1-31): "))

    fecha = mes * 100 + dia

    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Invierno" if hemisferio == "N" else "Verano"
    elif 321 <= fecha <= 620:
        estacion = "Primavera" if hemisferio == "N" else "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Verano" if hemisferio == "N" else "Invierno"
    elif 921 <= fecha <= 1220:
        estacion = "Otoño" if hemisferio == "N" else "Primavera"
    else:
        estacion = "Fecha inválida"

    print(f"En el hemisferio {hemisferio}, el {dia}/{mes} corresponde a {estacion}.")


