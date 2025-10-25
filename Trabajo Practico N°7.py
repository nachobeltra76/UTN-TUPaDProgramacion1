#Ejercicio 1 
precios_frutas = {'Banana': 1200,'Ananá': 2500, 'Melón': 3000, 'Uva':1450 }

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800
print(precios_frutas)


#Ejercicio 3 
lista_fruta = list(precios_frutas.keys())
print(lista_fruta)


#Ejercicio 4  
contactos = {}
for i in range (0,5):
    if i != 5: 
        key = input("Ingrese el nombre del contacto que desea agregar: ")
        value = input("Ingrese el numero del contacto que desea agregar: ")
        contactos[key] = value

adivinar = input("Ingrese un nombre para saber si esta en sus contactos: ")

if adivinar in contactos:
    print("Esa persona esta en sus contactos")
else:
    print("Esa persona no esta en sus contactos")


#Ejercicio 5 
frase = input("ingrese una frase: ")
palabras = frase.split() # con esto separo toda la frase en palabras 



recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else: 
        recuento[palabra] = 1

palabras_unicas = {palabra for palabra, cantidad in recuento.items() if cantidad == 1}

print("Palabras unicas = ", palabras_unicas)     
print("Recuento de palabras unicas:", recuento)


# Ejercicio 6 
alumnos = {}
acum = 0
for i in range (0,3):
    if i != 3: 
        key = input("Ingrese el nombre del alumno que desea agregar: ")
        lista_con_notas = []

        for x in range (0,3):
            if i != 3:
                nota = int(input("Ingrese las notas del alumno que desea agregar: "))
                lista_con_notas.append(nota)
                acum += nota
            promedio = acum / 3
        print(f"El promedio del alumno es: " , round(promedio,2))
        
    alumnos[key] = lista_con_notas       

print(alumnos)


# Ejercicio 7 
parcial_uno = {10,6,7,3,4,5,8}
parcial_dos = {10,6,7,8,9,4,5}

for alumno in range (len(parcial_uno)):
    if alumno in parcial_dos:
        if parcial_uno[alumno] >= 6 and parcial_dos[alumno] >= 6:
            print(f"El alumno {parcial_uno[alumno]} aprobó ambos parciales.")

# no supe como resolver este ejercicio con set 



# Ejercicio 8 
stock = {'pizza' : 10, 'perfume' : 9}
agregar = input("Desea agregar un producto? SI/NO: ")
agregar = agregar.lower()

if agregar == "si":
    producto_a_agregar = input("Ingrese el NOMBRE del producto que desea agregar: ")
    cant_de_prod_nuevo = input("Ingrese la CANTIDAD del producto que desea agregar: ")
    stock[producto_a_agregar] = cant_de_prod_nuevo


agregar_al_existente = input("Desea agregar unidades a un produccto existente? SI/NO: ")
agregar_al_existente = agregar_al_existente.lower()
if agregar_al_existente == "si":
        prod_existente = input("Ingrese el NOMBRE del producto  existente que desea modificar: ")
        cant_de_prod_exist = input("Ingrese la nueva CANTIDAD del producto exitente: ")
        stock[prod_existente] = cant_de_prod_exist

mostrar_stock = input("Desea ver el stock? SI/NO: ")
mostrar_stock = mostrar_stock.lower()
if (mostrar_stock == "si"):
    print (stock)



# Ejercicio 9 
agenda = {
    ("lunes", "10:00"): "reunion del trabajo",
    ("martes", "14:30"): "clase de programación",
    ("miércoles", "09:00"): "clase de gimnasio",
    ("viernes", "18:00"): "clase en el club"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")

evento = agenda.get((dia, hora))

evento = agenda.get((dia, hora))

if evento:
    print(f"Actividad programada: {evento}")
else:
    print("No hay actividad registrada en ese horario.")


# Ejercicio 10 
paises  = {"argentina" : "buenos aires" , "chile" : "santiago"}

capitales = {}
for pais, capital in paises.items():
    if capital in capitales:
        capitales[capital].append(pais)
    else:
        capitales[capital] = [pais]

print(paises)
print(capitales)
