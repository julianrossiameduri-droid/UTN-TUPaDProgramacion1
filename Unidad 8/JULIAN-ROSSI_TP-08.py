# Práctica – Programación I – Archivos

def crear_archivo_inicial():
    """1. Crea el archivo productos.txt con tres productos iniciales"""
    productos_iniciales = [
        "Lapicera,120.5,30\n",
        "Cuaderno,500,15\n",
        "Goma,80,50\n"
    ]
    with open("productos.txt", "w") as archivo:
        archivo.writelines(productos_iniciales)
    print("Archivo 'productos.txt' creado con datos iniciales.\n")


def leer_y_mostrar_productos():
    """2. Lee productos.txt y muestra los productos en formato legible"""
    try:
        with open("productos.txt", "r") as archivo:
            lineas = archivo.readlines()

        print("Productos actuales:")
        for linea in lineas:
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
        print()
    except FileNotFoundError:
        print("El archivo 'productos.txt' no existe. Crealo primero con la opción 1.\n")


def agregar_producto():
    """3. Agrega un nuevo producto al archivo sin borrar el contenido existente"""
    nombre = input("Nombre del producto: ").strip()
    precio = input("Precio: ").strip()
    cantidad = input("Cantidad: ").strip()

    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")

    print(f"Producto '{nombre}' agregado correctamente.\n")


def cargar_lista_diccionarios():
    """4. Carga los productos del archivo en una lista de diccionarios"""
    productos = []
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
    except FileNotFoundError:
        print("El archivo 'productos.txt' no existe.\n")
    return productos


def buscar_producto(lista_productos):
    """5. Busca un producto por nombre dentro de la lista de diccionarios"""
    nombre = input("Ingresá el nombre del producto a buscar: ").strip().lower()
    encontrado = False

    for p in lista_productos:
        if p["nombre"].lower() == nombre:
            print(f"Producto encontrado:")
            print(f"Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}\n")
            encontrado = True
            break

    if not encontrado:
        print("El producto no existe en el archivo.\n")


def guardar_productos_actualizados(lista_productos):
    """6. Sobrescribe el archivo productos.txt con los productos de la lista"""
    with open("productos.txt", "w") as archivo:
        for p in lista_productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("Archivo actualizado correctamente.\n")


# -----------------------------------------------------------
# Programa principal con menú
def menu():
    while True:
        print("=== GESTIÓN DE PRODUCTOS ===")
        print("1. Crear archivo inicial")
        print("2. Leer y mostrar productos")
        print("3. Agregar producto")
        print("4. Cargar productos en lista de diccionarios")
        print("5. Buscar producto por nombre")
        print("6. Guardar productos actualizados")
        print("0. Salir")

        opcion = input("Elegí una opción: ").strip()
        print()

        if opcion == "1":
            crear_archivo_inicial()
        elif opcion == "2":
            leer_y_mostrar_productos()
        elif opcion == "3":
            agregar_producto()
        elif opcion == "4":
            lista = cargar_lista_diccionarios()
            print(lista, "\n")
        elif opcion == "5":
            lista = cargar_lista_diccionarios()
            buscar_producto(lista)
        elif opcion == "6":
            lista = cargar_lista_diccionarios()
            guardar_productos_actualizados(lista)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.\n")


if __name__ == "__main__":
    menu()
