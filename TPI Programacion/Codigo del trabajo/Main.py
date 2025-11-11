import csv
import os
ARCHIVO_CSV = "paises.csv"
import Funciones


# Ejecuccion del programa

en_ejeccucion = True

lista_paises = Funciones.obtenerPaises()

while en_ejeccucion == True:
    print("-" * 40)
    print("Gestion de Paises - Menu Principal")
    print("-" * 40)
    print("1. Agregar un pais")
    print("2. Actualizar datos de la poblacion o superficie: ")
    print("3. Buscar un pais por nombre: ")
    print("4. Filtras paises ")
    print("5. Ordenar paises")
    print("6. Ver estadisticas")
    print("7. SALIR")

    entrada = (input("ingrese una opcion: "))

    if not entrada.isdigit(): # Si ingresan un string como opcion no rompe 
        print("Debe ingresar un numero!")
        continue
    
    opcion = int(entrada)
    
    if opcion not in [1, 2, 3, 4, 5, 6, 7]: # Sino ingresas una opcion ivalida te pide de vuelta
        print("Opcion invalida, intente nuevamente")
        continue

    match opcion:
        case 1:
            nombrePais = input("Ingrese el nombre del pais: ") # solicita el nombre y hace validaciones 
            nombrePais = Funciones.normalizarString(nombrePais)
            while nombrePais == "":
                print("Caracteres invalidos, ingrese el nombre de un pais: ")
                nombrePais = input("Ingrese el nombre del pais: ")
                nombrePais = Funciones.normalizarString(nombrePais)


            poblacionPais = input("Ingrese la poblacion del pais: ") # Solicita la poblacion y hace validaciones 
            poblacionPais = Funciones.normalizarInt(poblacionPais)
            while poblacionPais <= 0:
                print("Caracteres invalidos o negativos. Ingrese la poblacion del pais ")
                poblacionPais = input("Ingrese la poblacion del pais: ")
                poblacionPais = Funciones.normalizarInt(poblacionPais)


            superficiePais = input("Ingrese la superficie del pais: ") # Solicita la superficie y hace validaciones 
            superficiePais = Funciones.normalizarInt(superficiePais)
            while superficiePais <= 0:
                print("Caracteres invalidos o negativos. Ingrese la superficie del pais ")
                superficiePais = input("Ingrese la superficie del pais: ")
                superficiePais = Funciones.normalizarInt(superficiePais)


            continentePais = input("Ingrese el nombre del contienente del pais: ") # Solicita el continente y hace validaciones 
            continentePais = Funciones.normalizarString(continentePais)
            while continentePais == "":
                print("Caracteres invalidos, ingrese el contienente al que pertenece el pais: ")
                continentePais = input("Ingrese el contienente al que pertenece el pais: ")
                continentePais = Funciones.normalizarString(continentePais)


            # Una vez pasa las validaciones sino esta repetido, lo agrega al diccionario
            if not Funciones.paisYaExiste(nombrePais, lista_paises):
                    pais = { 
                    "NOMBRE": nombrePais,
                    "POBLACION" : poblacionPais,
                    "SUPERFICIE" : superficiePais,
                    "CONTINENTE" : continentePais
                    }
                    print("Se agrego correctamente el nuevo pais")
                    lista_paises.append(pais)
                    Funciones.guardarPaises(ARCHIVO_CSV, lista_paises) # Guardo los cambios realizados 

            else:
                print("Ese pais ya esta cargado en la lista de paises")

            
        case 2:
            print("Ingrese 1 si desea actualizar la POBLACION de un pais")
            print("Ingrese 2 si desea actualizar la SUPERFICIE de un pais")
            operacion = input("Seleccione que operacion desea realizar 1/2: ")

            while Funciones.normalizarInt(operacion) not in [1, 2]:
                print("Ingrese una opcion valida.")
                operacion = input("Seleccione que operacion desea realizar 1/2: ")

            operacion = int(operacion)

            if operacion == 1: # POBLACION
                pais_a_actualizar = input("Ingrese el nombre del pais que desea actualizar su poblacion: ")
                pais_a_actualizar = Funciones.normalizarString(pais_a_actualizar)
                existe = Funciones.paisYaExiste(pais_a_actualizar,lista_paises)

                nueva_cant_poblacion = Funciones.normalizarInt(input("Ingrese la nueva cantidad de población: "))
                while nueva_cant_poblacion == -1:
                    print("Ingrese un número mayor que 0")
                    nueva_cant_poblacion = Funciones.normalizarInt(input("Ingrese la nueva cantidad de población: "))

                

                if existe:
                    for pais in lista_paises:
                        if pais["NOMBRE"] == pais_a_actualizar:
                            pais["POBLACION"] = nueva_cant_poblacion
                    print("Se actualizo correctamente la poblacion")
                    Funciones.guardarPaises(ARCHIVO_CSV, lista_paises) # Guardo los cambios realizados 

                else:
                    print("Ese pais no existe en la lista")

            
            if operacion == 2: # SUPERFICIE
                pais_a_actualizar = input("Ingrese el nombre del pais que desea actualizar su superficie: ")
                pais_a_actualizar = Funciones.normalizarString(pais_a_actualizar)
                existe = Funciones.paisYaExiste(pais_a_actualizar,lista_paises)

                nueva_cant_superficie = Funciones.normalizarInt(input("Ingrese la nueva cantidad de superficie: "))
                while nueva_cant_superficie == -1:
                    print("Ingrese un número mayor que 0")
                    nueva_cant_superficie = Funciones.normalizarInt(input("Ingrese la nueva cantidad de superficie: "))


                if existe:
                    for pais in lista_paises:
                        if pais["NOMBRE"] == pais_a_actualizar:
                            pais["SUPERFICIE"] = nueva_cant_superficie
                    print("Se actualizo correctamente la superficie")
                    Funciones.guardarPaises(ARCHIVO_CSV, lista_paises) # Guardo los cambios realizados 
                else:
                    print("Ese pais no existe en la lista")

        case 3:
            pais_a_buscar = input("Ingrese el nombre del pais que esta buscando: ")
            pais_a_buscar = Funciones.normalizarString(pais_a_buscar)
            coincidencias = Funciones.buscarCoincidenciasPorNombre(pais_a_buscar,lista_paises)
            
            while pais_a_buscar == "":
                print("Caracter invalido")
                pais_a_buscar = input("Ingrese el nombre del pais que esta buscando: ")
                pais_a_buscar = Funciones.normalizarString(pais_a_buscar)
                

            if not coincidencias:
                print("No se encontro ninguna coincidencia con el nombre del pais ingresado.")
                continue
            else:
                if len(coincidencias) == 1:
                    pais = coincidencias[0]
                    print("Encontramos el pais que buscas")
                    print(f"País: {pais['NOMBRE']} | Población: {pais['POBLACION']} | Superficie: {pais['SUPERFICIE']} | Continente: {pais['CONTINENTE']}")
                else:
                    print("Se encontraron las siguientes coincidencias:")
                    for i, pais in enumerate(coincidencias):
                        print(f"{i+1}. {pais['NOMBRE']}")
                        
                    seleccion = input("Ingrese la opccion del PAIS que esta buscando: ")
                    seleccion = Funciones.normalizarInt(seleccion)

                    while seleccion == "" or not (1 <= seleccion <= len(coincidencias)):
                        print("Opción inválida. Debe ingresar un número entre 1 y", len(coincidencias))
                        seleccion = input("Ingrese la opccion del PAIS que esta buscando: ")
                        seleccion = Funciones.normalizarInt(seleccion)

                    else:
                        pais = coincidencias[seleccion - 1]
                        print("Mostrando información del país seleccionado:")
                        print(f"País: {pais['NOMBRE']} | Población: {pais['POBLACION']} | Superficie: {pais['SUPERFICIE']} | Continente: {pais['CONTINENTE']}")



        case 4:
            print("Presione 1 si desea filtrar paises por CONTINENTE")
            print("Presione 2 si desea filtrar paises por rango de POBLACION")
            print("Presione 3 si desea filtrar paises por rango de SUPERFICIE")
            opcion_filtrado = input("Ingrese la opcion 1/2/3: ")

            while Funciones.normalizarInt(opcion_filtrado) not in [1, 2, 3]:
                print("Ingrese una opcion valida.")
                opcion_filtrado = input("Ingrese la opcion 1/2/3: ")

            opcion_filtrado = Funciones.normalizarInt(opcion_filtrado)

            if opcion_filtrado == 1: # Filtro por CONTINENTE 
                print("Presione 1 si desea ver los paises del CONTINENTE ÁMERICANO")
                print("Presione 2 si desea ver los paises del CONTINENTE EUROPEO")
                print("Presione 3 si desea ver los paises del CONTINENTE ASIATICO")
                print("Presione 4 si desea ver los paises del CONTINENTE OCEANICO")
                print("Presione 5 si desea ver los paises del CONTINENTE ÁFRICANO")
                opcion_continente = input("Ingrese una de las opciones 1/2/3/4/5: ")

                while Funciones.normalizarInt(opcion_continente) not in [1,2,3,4,5]:
                    print("Ingrese una opcion valida.")
                    opcion_continente = input("Ingrese una de las opciones 1/2/3/4/5: ")

                opcion_continente = Funciones.normalizarInt(opcion_continente)

                if opcion_continente == 1:
                    continente = "america"
                    paises = Funciones.filtrarPorContinente(continente, lista_paises)
                    print(f"\nPaíses del continente {continente}:\n")
                    for i, pais in enumerate(paises, start=1):
                        print(f"{i}. {pais}")
                
                if opcion_continente == 2:
                    continente = "europa"
                    paises = Funciones.filtrarPorContinente(continente, lista_paises)
                    print(f"\nPaíses del continente {continente}:\n")
                    for i, pais in enumerate(paises, start=1):
                        print(f"{i}. {pais}")
                
                if opcion_continente == 3:
                    continente = "asia"
                    paises = Funciones.filtrarPorContinente(continente, lista_paises)
                    print(f"\nPaíses del continente {continente}:\n")
                    for i, pais in enumerate(paises, start=1):
                        print(f"{i}. {pais}")
                                
                if opcion_continente == 4:
                    continente = "oceania"
                    paises = Funciones.filtrarPorContinente(continente, lista_paises)
                    print(f"\nPaíses del continente {continente}:\n")
                    for i, pais in enumerate(paises, start=1):
                        print(f"{i}. {pais}")

                if opcion_continente == 5:
                    continente = "africa"
                    paises = Funciones.filtrarPorContinente(continente, lista_paises)
                    print(f"\nPaíses del continente {continente}:\n")
                    for i, pais in enumerate(paises, start=1):
                        print(f"{i}. {pais}")


            if opcion_filtrado == 2: # Filtro por RANGO DE POBLACION 
                rango_minimo = input("Ingrese el rango MINIMO: ")
                rango_maximo = input("Ingrese el rango MAXIMO: ")

                while Funciones.normalizarInt(rango_minimo) and Funciones.normalizarInt(rango_minimo) < 0:
                    print("No puede ingresar un rango negativo.")
                    rango_minimo = input("Ingrese el rango MINIMO: ")
                    rango_maximo = input("Ingrese el rango MAXIMO: ")

                rango_minimo = Funciones.normalizarInt(rango_minimo)
                rango_maximo = Funciones.normalizarInt(rango_maximo)

                paises_filtados_por_rango = Funciones.filtoPorRangoPoblacion(lista_paises, rango_minimo , rango_maximo)
                print(f"\nPaises filtrados de {rango_minimo} a {rango_maximo}:\n")
                for i, paises_filtados_por_rango in enumerate(paises_filtados_por_rango, start=1):
                    print(f"{i}. {paises_filtados_por_rango}")
                

            if opcion_filtrado == 3: # Filtro por RANGO DE SUPERFICIE 
                rango_minimo = input("Ingrese el rango MINIMO: ")
                rango_maximo = input("Ingrese el rango MAXIMO: ")

                while Funciones.normalizarInt(rango_minimo) and Funciones.normalizarInt(rango_minimo) < 0:
                    print("No puede ingresar un rango negativo.")
                    rango_minimo = input("Ingrese el rango MINIMO: ")
                    rango_maximo = input("Ingrese el rango MAXIMO: ")

                rango_minimo = Funciones.normalizarInt(rango_minimo)
                rango_maximo = Funciones.normalizarInt(rango_maximo)

                paises_filtados_por_rango = Funciones.filtoPorRangoSuperficie(lista_paises, rango_minimo , rango_maximo)
                print(f"\nPaises filtrados de {rango_minimo} a {rango_maximo}:\n")
                for i, paises_filtados_por_rango in enumerate(paises_filtados_por_rango, start=1):
                    print(f"{i}. {paises_filtados_por_rango}")


        case 5:
            print("Presione 1 si desea ordenar paises por NOMBRE")
            print("Presione 2 si desea ordenar paises por rango de POBLACION")
            print("Presione 3 si desea ordenar paises por rango de SUPERFICIE")
            opcion_filtrado = input("Ingrese la opcion 1/2/3: ")

            while Funciones.normalizarInt(opcion_filtrado) not in [1, 2, 3]:
                print("Ingrese una opcion valida.")
                opcion_filtrado = input("Ingrese la opcion 1/2/3: ")
            
            opcion_filtrado = Funciones.normalizarInt(opcion_filtrado)

            if opcion_filtrado == 1: # Ordenado por NOMBRE
                paises_ordenados_por_nombre = Funciones.ordenoPaisPorNombre(lista_paises)
                print("\nPaises ordenados por NOMBRE:\n")
                for pais in paises_ordenados_por_nombre:
                    print(f"{{'NOMBRE' : '{pais['NOMBRE']}', 'POBLACION' : {pais['POBLACION']}, 'SUPERFICIE' : {pais['SUPERFICIE']}, 'CONTINENTE' : '{pais['CONTINENTE']}'}}")
               

            if opcion_filtrado == 2: # Ordenado por POBLACION
                print("Ingrese 1 si desea ordenarlo de forma ASCEDENTE")
                print("Ingrese 2 si desea ordenarlo de forma DESCENDENTE")
                opcion_orden = input("Ingrese la opcion que desea 1/2: ")

                while Funciones.normalizarInt(opcion_orden) not in [1, 2]:
                    print("Ingrese una opcion valida.")
                    opcion_orden =input("Ingrese la opcion que desea 1/2: ")
                
                opcion_orden = Funciones.normalizarInt(opcion_orden)

                if opcion_orden == 1: # Por poblacion ASCENDENTE 
                    paises_ordenados_por_poblacion = Funciones.ordenoPaisPorPoblacion(lista_paises,opcion_orden)
                    print("\nPaises ordenados por orden POBLACION:\n")
                    for pais in paises_ordenados_por_poblacion:
                        print(f"{{'NOMBRE' : '{pais['NOMBRE']}', 'POBLACION' : {pais['POBLACION']}, 'SUPERFICIE' : {pais['SUPERFICIE']}, 'CONTINENTE' : '{pais['CONTINENTE']}'}}")
                
                if opcion_orden == 2: # por poblacion DESCENDENTE 
                    paises_ordenados_por_poblacion = Funciones.ordenoPaisPorPoblacion(lista_paises,opcion_orden)
                    print("\nPaises ordenados por orden POBLACION:\n")
                    for pais in paises_ordenados_por_poblacion:
                        print(f"{{'NOMBRE' : '{pais['NOMBRE']}', 'POBLACION' : {pais['POBLACION']}, 'SUPERFICIE' : {pais['SUPERFICIE']}, 'CONTINENTE' : '{pais['CONTINENTE']}'}}")


            if opcion_filtrado == 3: # Ordenado por SUPERFICIE
                print("Ingrese 1 si desea ordenarlo de forma ASCEDENTE")
                print("Ingrese 2 si desea ordenarlo de forma DESCENDENTE")
                opcion_orden = input("Ingrese la opcion que desea 1/2: ")

                while Funciones.normalizarInt(opcion_orden) not in [1, 2]:
                    print("Ingrese una opcion valida.")
                    opcion_orden = input("Ingrese la opcion que desea 1/2: ")
                
                opcion_orden = Funciones.normalizarInt(opcion_orden)

                if opcion_orden == 1: # Por superficie ASCENDENTE 
                    paises_ordenados_por_superficie = Funciones.ordenoPaisPorPoblacion(lista_paises,opcion_orden)
                    print("\nPaises ordenados por orden SUPERFICIE:\n")
                    for pais in paises_ordenados_por_superficie:
                        print(f"{{'NOMBRE' : '{pais['NOMBRE']}', 'POBLACION' : {pais['POBLACION']}, 'SUPERFICIE' : {pais['SUPERFICIE']}, 'CONTINENTE' : '{pais['CONTINENTE']}'}}")

                if opcion_orden == 2: # Por superficie ASCENDENTE 
                    paises_ordenados_por_superficie = Funciones.ordenoPaisPorPoblacion(lista_paises,opcion_orden)
                    print("\nPaises ordenados por orden SUPERFICIE:\n")
                    for pais in paises_ordenados_por_superficie:
                        print(f"{{'NOMBRE' : '{pais['NOMBRE']}', 'POBLACION' : {pais['POBLACION']}, 'SUPERFICIE' : {pais['SUPERFICIE']}, 'CONTINENTE' : '{pais['CONTINENTE']}'}}")

                
        case 6:
            print("Presione 1 si desea ver el pais con MAYOR y con MENOR cantidad de poblacion")
            print("Presione 2 si desea ver el PROMEDIO de POBLACION de todos los paises")
            print("Presione 3 si desea ver el PROMEDIO de SUPERFICIE de todos los paises")
            print("Presione 4 si desea ver la CANTIDAD de paises por CONTINENTE")
            opcion_estadistica = input("Ingrese la opcion 1/2/3/4: ")

            while Funciones.normalizarInt(opcion_estadistica) not in [1, 2, 3, 4]:
                print("Ingrese una opcion valida.")
                opcion_estadistica = input("Ingrese la opcion que desea 1/2/3/4: ")

            opcion_estadistica = Funciones.normalizarInt(opcion_estadistica)
            
            if opcion_estadistica == 1:
                pais_con_mayor_poblacion = Funciones.mayorPoblacion(lista_paises)
                pais_con_menor_poblacion = Funciones.menorPoblacion(lista_paises)
                print(f"El pais con MAYOR poblacion es: {pais_con_mayor_poblacion}")
                print(f"El pais con MENOR poblacion es: {pais_con_menor_poblacion}")

            if opcion_estadistica == 2:
                promedio_poblacion = Funciones.promedioPoblacion(lista_paises)
                print(f"El promedio de poblacion de todos los paises es: {promedio_poblacion:.2f}")
            
            if opcion_estadistica == 3:
                promedio_superficie = Funciones.promedioSuperficie(lista_paises)
                print(f"El promedio de superficie de todos los paises es: {promedio_superficie:.2f}")
            
            if opcion_estadistica == 4:
                cant_paises_por_continente = Funciones.cantPaisesPorContinente(lista_paises)
                print(cant_paises_por_continente)


        case 7:
            print("Saliendo de la aplicacion...")
            print("El programa se finalizo correctamente")
            en_ejeccucion = False


