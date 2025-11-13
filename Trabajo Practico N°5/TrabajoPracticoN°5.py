import random
# # EJERCICIO 1 
# notas = [8,3,5,3,5,8,10,9,1,4]
# print (notas)

# acum = 0
# alta = 0
# baja = 11

# for i in range (0,10):
#     acum += notas[i]  # Acumulo total de las notas

#     if notas[i] > alta:
#         alta = notas[i]

#     if notas[i] < baja:
#         baja = notas[i]

# promedio= acum / 10
# print("promedio = ", promedio)
# print("notas mas alta  = ", alta)
# print("notas mas baja = ", baja)


# # EJERCICIO 2
# productos = []

# for i in range (5):
#     prod = input("ingrese un producto: ")
#     productos.append(prod)

# ordenados = sorted(productos)
# print(ordenados)

# eliminar = input("Qué producto desea eliminar?: ")
# if eliminar in productos:
#     productos.remove(eliminar)
#     print("se elimino correctamente")
# else:
#     print("ese producto no esta en la lista")

# ordenados = sorted(productos)
# print(ordenados)


# # EJERCICIO 3 
# lista_random = []
# pares = []
# inpares = []

# for i in range (15):
#     num = random.randint(1,100)
#     lista_random.append(num)

#     if num % 2 == 0:
#         pares.append(num)
#     else:
#         inpares.append(num)
    

# print(lista_random)
# print(pares, " - Cant pares: ", len(pares))
# print(inpares, " - Cant inpares: ", len(inpares))


# # EJERCICIO 4 
# lista = [1,3,4,3,5,8,7,7,8,9,10]
# sin_duplicados = []
# x = 0
# for i in range (len(lista)):
#     x = i 
#     i = lista[i]
#     if x != i:
#         sin_duplicados.append(i)
#     x = i 
# print(sin_duplicados)


# # EJERCICIO 5 
# alumnos = []

# for i in range(8):
#     alumn = input("Ingrese un el nombre del alumno: ")
#     alumnos.append(alumn)


# agregar = input("Desea agregar un nuevo alumno? SI/NO: ")
# alumno_agregar = input("ingrese el nuevo alumno: ")
# if agregar.lower() == "si":
#     alumnos.append(alumno_agregar)
#     print("se agrego correctamente")

# print(alumnos)


# # EJERCICIO 6 
# numeros = [10, 20, 30, 40, 50, 60, 70]
# numeros = [numeros[-1]] + numeros[:-1]
# print(numeros)


# # EJERCICIO 7
# temperaturas = [
#     [10, 22],  
#     [12, 25],  
#     [9, 20],   
#     [11, 24],  
#     [13, 26], 
#     [8, 19],   
#     [10, 23]   
# ]

# acum_max= 0 
# for dia in temperaturas:
#     acum_max += dia[1] # acumulo la maxima 

# promedio_maxima = acum_max // 7

# acum_min= 0 
# for dia in temperaturas:
#     acum_min += dia[0] # acumulo la minima 

# promedio_minima = acum_min // 7

# print("promedio maxima: ", promedio_maxima)
# print("promedio minima: ", promedio_minima)


# EJERCICIO 8 
# notas = [
#     [7, 8, 6],  
#     [5, 9, 7],  
#     [6, 6, 6], 
#     [8, 7, 9],  
#     [9, 10, 8]  
# ]

# contador = 1 
# print("Promedio por estudiante:")
# for alumno in notas: 
#     promedio = sum(alumno) / len(alumno)
#     print(f"estudiante {contador}: {promedio:.2f}")
#     contador += 1

# print("\nPromedio por materia:")
# for j in range(3):  
#     suma = 0
#     for i in range(5):  
#         suma += notas[i][j]
#     promedio = suma / 5
#     print(f"Materia {j+1}: {promedio:.2f}")



# EJERCICIO 9 
# # Crear matriz vacía 3x3
# tablero = [
#     ["-", "-", "-"],
#     ["-", "-", "-"],
#     ["-", "-", "-"]
# ]

# # Mostrar tablero
# def mostrar_tablero(matriz):
#     print("\nTablero actual:")
#     for fila in matriz:
#         print(" | ".join(fila))
#     print()

# mostrar_tablero(tablero)

# for turno in range(9):
#     jugador = "X" if turno % 2 == 0 else "O"
#     print(f"turno del jugador {jugador}")

#     while True:
#         fila = int(input("ingrese la fila en la que se quiere posicionar (0 a 2): "))
#         columna = int(input("Iingrese la columna en la que se quiere posicionar  (0 a 2): "))

#         if 0 <= fila <= 2 and 0 <= columna <= 2:
#             if tablero[fila][columna] == "-":
#                 tablero[fila][columna] = jugador
#                 break
#             else:
#                 print("no podes posicionarte en esa casilla, elegi otra")
#         else:
#             print("esa posicion no existe, usa valores entre 0 y 2.")

#     mostrar_tablero(tablero)


# EJERCICIO 10 
# ventas = [
#     [5, 3, 4, 6, 2, 7, 5], 
#     [2, 4, 3, 5, 6, 4, 3],  
#     [6, 5, 7, 4, 3, 2, 6],  
#     [3, 2, 5, 6, 4, 3, 2]   
# ]

# print("total por producto:")
# for i in range(4):
#     total = sum(ventas[i])
#     print(f"Producto {i+1}: {total}")

# totales_dia = []
# for j in range(7):
#     dia = ventas[0][j] + ventas[1][j] + ventas[2][j] + ventas[3][j]
#     totales_dia.append(dia)

# mayor_dia = max(totales_dia)
# dia_mayor = totales_dia.index(mayor_dia) + 1
# print(f"\ndia con mas ventas: dia {dia_mayor} con {mayor_dia} unidades")

# totales_producto = [sum(p) for p in ventas]
# mas_vendido = max(totales_producto)
# producto_mayor = totales_producto.index(mas_vendido) 
# print(f"producto mas vendido: Producto {producto_mayor} con {mas_vendido} unidades")