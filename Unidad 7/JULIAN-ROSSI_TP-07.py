# 1) Agregar frutas al diccionario de precios
def punto_1():
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    # Agregados
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300
    return precios_frutas


# ------------------------------------------------------------------
# 2) Actualizar precios en el diccionario resultante del punto 1
def punto_2(precios_frutas):
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800
    return precios_frutas


# ------------------------------------------------------------------
# 3) Crear una lista únicamente con las frutas (sin precios)
def punto_3(precios_frutas):
    return list(precios_frutas.keys())


# ------------------------------------------------------------------
# 4) Agenda telefónica simple: cargar 5 contactos y consultar uno
def cargar_contactos_telefonicos(cantidad=5):
    agenda = {}
    for i in range(1, cantidad + 1):
        nombre = input("Nombre del contacto {}: ".format(i)).strip()
        numero = input("Número de {}: ".format(nombre)).strip()
        agenda[nombre] = numero
    return agenda

def consultar_contacto(agenda):
    nombre = input("Ingresá el nombre a buscar: ").strip()
    if nombre in agenda:
        print("El número de {} es: {}".format(nombre, agenda[nombre]))
    else:
        print("No existe un contacto llamado {} en la agenda.".format(nombre))


# ------------------------------------------------------------------
# 5) Frase: mostrar palabras únicas (set) y un diccionario de frecuencias
def analizar_frase():
    frase = input("Ingresá una frase: ").strip().lower()
    # Separación básica por espacios (sin limpiar puntuación para no usar imports)
    palabras = [p for p in frase.split() if p != ""]
    palabras_unicas = set(palabras)
    # Conteo manual
    frecuencias = {}
    for p in palabras:
        if p in frecuencias:
            frecuencias[p] += 1
        else:
            frecuencias[p] = 1
    print("Palabras únicas:", palabras_unicas)
    print("Frecuencias:", frecuencias)
    return palabras_unicas, frecuencias


# ------------------------------------------------------------------
# 6) Ingresar 3 alumnos y una tupla de 3 notas para cada uno. Mostrar promedio.
def promedios_alumnos():
    alumnos = {}
    for i in range(1, 4):
        nombre = input("Nombre del alumno {}: ".format(i)).strip()
        print("Ingresá 3 notas (enter separa cada una) para {}:".format(nombre))
        n1 = float(input("Nota 1: ").strip())
        n2 = float(input("Nota 2: ").strip())
        n3 = float(input("Nota 3: ").strip())
        alumnos[nombre] = (n1, n2, n3)
    print("Promedios:")
    for nombre, notas in alumnos.items():
        promedio = (notas[0] + notas[1] + notas[2]) / 3.0
        print("- {}: {:.2f}".format(nombre, promedio))
    return alumnos


# ------------------------------------------------------------------
# 7) Operaciones sobre sets de aprobados en Parcial 1 y Parcial 2
def analizar_aprobados(parcial1, parcial2):
    ambos = parcial1.intersection(parcial2)
    solo_uno = parcial1.symmetric_difference(parcial2)
    al_menos_uno = parcial1.union(parcial2)
    return ambos, solo_uno, al_menos_uno


# ------------------------------------------------------------------
# 8) Inventario de stock por producto
def gestionar_stock():
    stock = {}
    while True:
        print("\n--- STOCK ---")
        print("1) Consultar stock de un producto")
        print("2) Agregar unidades a producto existente")
        print("3) Agregar nuevo producto")
        print("0) Salir")
        op = input("Elegí una opción: ").strip()
        if op == "0":
            break
        elif op == "1":
            prod = input("Producto a consultar: ").strip()
            if prod in stock:
                print("Stock de {}: {}".format(prod, stock[prod]))
            else:
                print("El producto no existe.")
        elif op == "2":
            prod = input("Producto: ").strip()
            if prod in stock:
                try:
                    cant = int(input("Unidades a agregar: ").strip())
                except ValueError:
                    print("Cantidad inválida.")
                    continue
                stock[prod] += cant
                print("Nuevo stock de {}: {}".format(prod, stock[prod]))
            else:
                print("El producto no existe.")
        elif op == "3":
            prod = input("Nombre del nuevo producto: ").strip()
            try:
                cant = int(input("Stock inicial: ").strip())
            except ValueError:
                print("Cantidad inválida.")
                continue
            if prod in stock:
                print("Ya existe. Usá la opción 2 para sumar stock.")
            else:
                stock[prod] = cant
                print("Agregado {} con stock {}.".format(prod, cant))
        else:
            print("Opción inválida.")
    return stock


# ------------------------------------------------------------------
# 9) Agenda con claves (día, hora) -> evento. Consultar.
def agenda_eventos():
    agenda = {}
    print("Cargá eventos (dejá día vacío para terminar).")
    while True:
        dia = input("Día (ej: Lunes): ").strip()
        if dia == "":
            break
        hora = input("Hora (ej: 10:00): ").strip()
        evento = input("Evento: ").strip()
        clave = (dia, hora)
        agenda[clave] = evento

    print("\nConsulta de evento.")
    dia_c = input("Día: ").strip()
    hora_c = input("Hora: ").strip()
    clave_c = (dia_c, hora_c)
    if clave_c in agenda:
        print("En {} a las {}: {}".format(dia_c, hora_c, agenda[clave_c]))
    else:
        print("No hay evento cargado en esa fecha y hora.")
    return agenda


# ------------------------------------------------------------------
# 10) Invertir diccionario país->capital a capital->país
def invertir_paises_capitales(paises_capitales):
    invertido = {}
    for pais, capital in paises_capitales.items():
        invertido[capital] = pais
    return invertido


# ------------------------------------------------------------------
# Bloque de ejemplo (se puede comentar si sólo se quieren usar las funciones)
if __name__ == "__main__":
    print("Puntos 1, 2 y 3:")
    precios = punto_1()
    precios = punto_2(precios)
    frutas = punto_3(precios)
    print("Diccionario final:", precios)
    print("Sólo frutas:", frutas)

    print("\nPunto 7 (sets):")
    p1 = {"Ana", "Luis", "Marcos", "Sofía"}
    p2 = {"Sofía", "Marcos", "Julia", "Pedro"}
    ambos, solo_uno, al_menos_uno = analizar_aprobados(p1, p2)
    print("Aprobaron ambos:", ambos)
    print("Aprobaron sólo uno:", solo_uno)
    print("Aprobaron al menos uno:", al_menos_uno)

    print("\nPunto 10 (invertir diccionario país-capital):")
    paises = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia"}
    print("Original:", paises)
    print("Invertido:", invertir_paises_capitales(paises))