# TP 5 - Listas - Resolución en Python

# 1
notas = []
for i in range(10):
    nota = float(input("Ingrese nota: "))
    notas.append(nota)
print(notas)
suma = 0
for n in notas:
    suma += n
print("Promedio:", suma/len(notas))
print("Máxima:", max(notas))
print("Mínima:", min(notas))

print("-----")

# 2
productos = []
for i in range(5):
    prod = input("Ingrese producto: ")
    productos.append(prod)
print(sorted(productos))
elim = input("Producto a eliminar: ")
if elim in productos:
    productos.remove(elim)
print(productos)

print("-----")

# 3
import random
nums = []
for i in range(15):
    nums.append(random.randint(1,100))
pares = []
impares = []
for n in nums:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print("Pares:", len(pares))
print("Impares:", len(impares))

print("-----")

# 4
lista = [1,2,2,3,3,3,4,4,5]
sin_rep = []
for x in lista:
    if x not in sin_rep:
        sin_rep.append(x)
print(sin_rep)

print("-----")

# 5
alumnos = []
for i in range(8):
    alumnos.append(input("Ingrese nombre: "))
accion = input("Agregar(A) o Eliminar(E)?: ")
if accion.upper()=="A":
    alumnos.append(input("Nombre a agregar: "))
elif accion.upper()=="E":
    rem = input("Nombre a eliminar: ")
    if rem in alumnos:
        alumnos.remove(rem)
print(alumnos)

print("-----")

# 6
l = [1,2,3,4,5,6,7]
l = [l[-1]] + l[:-1]
print(l)

print("-----")

# 7
temps = []
for i in range(7):
    minimo = float(input("Min: "))
    maximo = float(input("Max: "))
    temps.append([minimo,maximo])
suma_min = 0
suma_max = 0
for t in temps:
    suma_min += t[0]
    suma_max += t[1]
print("Prom min:", suma_min/7)
print("Prom max:", suma_max/7)
ampls = []
for dia in temps:
    ampls.append(dia[1]-dia[0])
print("Mayor amplitud dia:", ampls.index(max(ampls))+1)

print("-----")

# 8
notas = []
for i in range(5):
    fila = []
    for j in range(3):
        fila.append(float(input("Nota: ")))
    notas.append(fila)
for fila in notas:
    print("Prom alumno:", sum(fila)/3)
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    print("Prom materia", j+1, "=", suma/5)

print("-----")

# 9
tres = [["-","-","-"],["-","-","-"],["-","-","-"]]
for turn in range(9):
    fila = int(input("Fila: "))
    col = int(input("Col: "))
    marca = input("X/O: ")
    tres[fila][col]=marca
    for fila in tres:
        print(fila)

print("-----")

# 10
ventas = []
for i in range(4):
    fila = []
    for j in range(7):
        fila.append(float(input("Venta: ")))
    ventas.append(fila)
for i in range(4):
    print("Total prod", i+1, "=", sum(ventas[i]))
tot_dias=[]
for j in range(7):
    s=0
    for i in range(4):
        s+=ventas[i][j]
    tot_dias.append(s)
print("Dia mas ventas:", tot_dias.index(max(tot_dias))+1)
tot_prod=[]
for i in range(4):
    tot_prod.append(sum(ventas[i]))
print("Prod mas vendido:", tot_prod.index(max(tot_prod))+1)
