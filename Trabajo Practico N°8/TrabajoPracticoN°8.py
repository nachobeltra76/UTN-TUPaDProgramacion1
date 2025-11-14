import csv
import os
ARCHIVO_CSV = "productos.txt"

# Funciones 

def obtenerProductos():
    if not os.path.exists(ARCHIVO_CSV):
        print("El archivo no existe. Se crea uno vacío con encabezados.")
        with open(ARCHIVO_CSV, "a", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["NOMBRE", "PRECIO", "CANTIDAD"])
            escritor.writeheader()

    catalogo = []
    with open(ARCHIVO_CSV, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            catalogo.append({
                "NOMBRE": fila["NOMBRE"],
                "PRECIO": int(fila["PRECIO"]),
                "CANTIDAD": int(fila["CANTIDAD"])
            })
    return catalogo

def guardarProductos(ARCHIVO_CSV, productos):
    with open(ARCHIVO_CSV, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ['NOMBRE', 'PRECIO', 'CANTIDAD']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for prod in productos:
            escritor.writerow({
                'NOMBRE': prod['NOMBRE'],
                'PRECIO': prod['PRECIO'],
                'CANTIDAD': prod['CANTIDAD']
            })

# Esta funcion se usa para validar si el string ingresado es correcto y luego normalizarlo, asi todo tiene un formato
def normalizarString(entrada):
    if not isinstance(entrada, str):
        return ""  # No es string

    entrada = entrada.strip()
    if entrada.isdigit():
        return ""  # Es un número aunque esté como string

    entrada_normalizada = " ".join(entrada.lower().split())
    return entrada_normalizada
# Esta funciona se usa para validar si el dato tipo INT es correcto y luego normalizarlo, asi todo tiene un formato
def normalizarInt(entrada):

    if isinstance(entrada, str) and entrada.strip().isdigit():
        valor = int(entrada.strip())
        if valor > 0:
            return valor
    return -1 # Devuelve -1 si es un STRING o MENOR QUE 0

def productoYaExiste(nombre, lista_prod):
    nombre = normalizarString(nombre)
    for prod in lista_prod:
        if normalizarString(prod["NOMBRE"]) == nombre:
            return True
    
    return False







# EJECCUCION DEL PROGRAMA PRINCIPAL

en_ejeccucion = True

lista_prod = obtenerProductos()

while en_ejeccucion == True:
    print("-" * 40)
    print("Gestor de productos - Menu Principal")
    print("-" * 40)
    print("1. Agregar un producto")
    print("2. Ver productos")
    print("3. Buscar productos x nombre")
    print("10. SALIR")

    entrada = (input("ingrese una opcion: "))

    if not entrada.isdigit(): # Si ingresan un string como opcion no rompe 
        print("Debe ingresar un numero!")
        continue
    
    opcion = int(entrada)
    
    if opcion not in [1, 2,3, 10]: # Sino ingresas una opcion ivalida te pide de vuelta
        print("Opcion invalida, intente nuevamente")
        continue

    match opcion: 
        case 1:
            nombreProd = input("Ingrese el nombre del producto: ") 
            nombreProd = normalizarString(nombreProd)

            while nombreProd == "":
                print("Caracteres invalidos, ingrese el nombre de un producto: ")
                nombreProd = input("Ingrese el nombre del producto: ")
                nombreProd = normalizarString(nombreProd)


            precioProd = input("Ingrese la precio del producto: ")  
            precioProd = normalizarInt(precioProd)
            while precioProd <= 0:
                print("Caracteres invalidos o negativos. Ingrese el precio del producto ")
                precioProd = input("Ingrese el precio del producto: ")
                precioProd = normalizarInt(precioProd)


            cantidadProd = input("Ingrese la cantidad del producto: ") 
            cantidadProd = normalizarInt(cantidadProd)
            while cantidadProd <= 0:
                print("Caracteres invalidos o negativos. Ingrese cantidad del producto ")
                cantidadProd = input("Ingrese cantidad del producto: ")
                cantidadProd = normalizarInt(cantidadProd)

            if not productoYaExiste(nombreProd, lista_prod):
                    prod = { 
                    "NOMBRE": nombreProd,
                    "PRECIO" : precioProd,
                    "CANTIDAD" : cantidadProd
                    }
                    print("Se agrego correctamente el nuevo producto")
                    lista_prod.append(prod)
                    guardarProductos(ARCHIVO_CSV, lista_prod) # Guardo los cambios realizados 

            else:
                print("Ese producto ya esta cargado en la lista de producto")

        case 2:
            print("Los productos disponibles son los siguientes: ")
            for i in range (0, len(lista_prod)):
                print(lista_prod[i])

        case 3: 
            nombreProd = input("Ingrese el nombre del producto que esta buscando: ") 
            nombreProd = normalizarString(nombreProd)

            while nombreProd == "":
                print("Caracteres invalidos, ingrese el nombre de un producto: ")
                nombreProd = input("Ingrese el nombre del producto: ")
                nombreProd = normalizarString(nombreProd)

            if not productoYaExiste(nombreProd,lista_prod):
                print("El producto que ingreso no existe")
            else:
                    for prod in lista_prod:
                        if prod["NOMBRE"] == nombreProd:
                            print("Se encontro el producto que estaba buscando: ")
                            print(lista_prod[i])

