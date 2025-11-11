import csv
import os
ARCHIVO_CSV = "paises.csv"

# Todas las funciones del programa 

# Esta funcion crea la lista de paises, tomandolo del CSV, en caso de que no exista lo crea 
def obtenerPaises():
    if not os.path.exists(ARCHIVO_CSV):
        print("El archivo no existe. Se crea uno vacío con encabezados.")
        with open(ARCHIVO_CSV, "a", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["NOMBRE", "POBLACION", "SUPERFICIE", "CONTINENTE"])
            escritor.writeheader()

    catalogo = []
    with open(ARCHIVO_CSV, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            catalogo.append({
                "NOMBRE": fila["NOMBRE"],
                "POBLACION": int(fila["POBLACION"]),
                "SUPERFICIE": int(fila["SUPERFICIE"]),
                "CONTINENTE": fila["CONTINENTE"]
            })
    return catalogo

# Esta funcion guarda cada cambio que se haga en la lista, para impactarla en el CSV
def guardarPaises(ARCHIVO_CSV, paises):
    with open(ARCHIVO_CSV, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ['NOMBRE', 'POBLACION', 'SUPERFICIE', 'CONTINENTE']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow({
                'NOMBRE': pais['NOMBRE'],
                'POBLACION': pais['POBLACION'],
                'SUPERFICIE': pais['SUPERFICIE'],
                'CONTINENTE': pais['CONTINENTE']
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


# Devuelve true si el pais ya esta cargado, false en caso de que no
def paisYaExiste(nombre, lista_paises):
    nombre = normalizarString(nombre)
    for pais in lista_paises:
        if normalizarString(pais["NOMBRE"]) == nombre:
            return True
    
    return False


def buscarCoincidenciasPorNombre(nombre_buscado, lista_paises):
    nombre_buscado = normalizarString(nombre_buscado)
    resultados = []

    for pais in lista_paises:
        nombre_actual = normalizarString(pais["NOMBRE"])
        if nombre_buscado in nombre_actual:  # Coincidencia parcial, tomamos como que una parte de la pais ingresado, coincida con la palabra real
            resultados.append(pais)

    return resultados

#Esta seguidilla de funciones se encarga de la logica de filtrar por continente,por rango de poblacion y superficie
#Ordenar por nombre Poblacion Superficie (Ascendente o Descendente)
#Mostrar Estadisticas del pais con mayor y menor poblacion
#Promedio de poblacion 
#Promedio de superficie
#Cantidad de Paises por continente

def filtrarPorContinente(continente,lista_paises):
    continente = normalizarString(continente)
    paise_filtrados = []
    for p in lista_paises:
        if p["CONTINENTE"] == continente:
            paise_filtrados.append(p) 
               
    return paise_filtrados
                                                                 

def filtoPorRangoPoblacion (lista_paises , rango_minimo , rango_maximo):
    paises_filtados = []
    for pais in lista_paises:
        if pais["POBLACION"] >= rango_minimo and pais["POBLACION"] <= rango_maximo:
            paises_filtados.append(pais)
    return paises_filtados


def filtoPorRangoSuperficie (lista_paises , rango_minimo , rango_maximo):
    paises_filtados = []
    for pais in lista_paises:
        if pais["SUPERFICIE"] >= rango_minimo and pais["SUPERFICIE"] <= rango_maximo:
            paises_filtados.append(pais)
    return paises_filtados

def obtenerNombre(pais):
    return pais["NOMBRE"]

def obtenerPoblacion(pais):
    return pais["POBLACION"]


def ordenoPaisPorNombre(lista_paises):
    paises_ordenados_por_nombre = sorted(lista_paises, key=obtenerNombre)
    return paises_ordenados_por_nombre

def ordenoPaisPorPoblacion(lista_paises,opcion):
    if opcion == 1: # Ascendente 
        paises_ordenados_por_poblacion = sorted(lista_paises, key=obtenerPoblacion)
        return paises_ordenados_por_poblacion
    
    if opcion == 2: # Descendente 
        paises_ordenados_por_poblacion = sorted(lista_paises, key=obtenerPoblacion, reverse=True) 
        return paises_ordenados_por_poblacion
    

def ordenPaisPorSuperficie (lista_paises , opcion):
    if opcion == 1: # Ascendente 
        paises_ordenados_por_superficie = sorted(lista_paises, key=obtenerPoblacion)
        return paises_ordenados_por_superficie
    
    if opcion == 2: # Descendente 
        paises_ordenados_por_superficie = sorted(lista_paises, key=obtenerPoblacion, reverse=True) 
        return paises_ordenados_por_superficie
    

def mayorPoblacion (lista_paises):
    pais_mayor = lista_paises[0]
    for pais in lista_paises:
        if pais["POBLACION"] > pais_mayor["POBLACION"]:
            pais_mayor = pais
    return pais_mayor

def menorPoblacion (lista_paises):
    pais_menor = lista_paises[0]
    for pais in lista_paises:
        if pais["POBLACION"] < pais_menor["POBLACION"]:
                pais_menor = pais
    return pais_menor

def promedioPoblacion(lista_paises):
    acum = 0 # Acumula la cantidad de poblacion
    cont = 0 # Cuenta la cantidad de paises 

    for pais in lista_paises:
        acum += pais["POBLACION"]
        cont += 1
    return acum / cont

def promedioSuperficie(lista_paises):
    acum = 0 # Acumula la cantidad de superficie
    cont = 0 # Cuenta la cantidad de paises 

    for pais in lista_paises:
        acum += pais["SUPERFICIE"]
        cont += 1
    return acum / cont

def cantPaisesPorContinente (lista_paises):
    contAmerica = 0 
    contEuropa = 0 
    contAsia = 0 
    contOceania = 0 
    contAfrica = 0 

    for pais in lista_paises:
        if pais["CONTINENTE"] == "america":
            contAmerica += 1
        if pais["CONTINENTE"] == "europa":
            contEuropa+= 1
        if pais["CONTINENTE"] == "asia":
            contAsia += 1
        if pais["CONTINENTE"] == "oceania":
            contOceania += 1
        if pais["CONTINENTE"] == "africa":
            contAfrica += 1

    contadores = [{"america" : contAmerica},{"europa":contEuropa},{"asia":contAsia},{"oceania" : contOceania}, {"africa" : contAfrica}]
    return contadores


    