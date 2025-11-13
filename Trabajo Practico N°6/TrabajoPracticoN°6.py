import math
# DEFINICION DE FUNCIONES 
def saludo ():
    return "Hola Mundo!"

def saludar_usuario(nombre):
    return "Hola " + nombre +"!"

def informacion_personal(nombre,apellido,edad,residencia):
    return "Soy " + nombre + apellido + " tengo " + edad + " años y vivo en " + residencia

def calcular_area_circulo(radio):
    return math.pi * radio **2 

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def segundos_a_horas(segundos):
    return segundos//3600

def tabla_multiplicar(numero):
    for i in range (1,11):
        print (numero , " x " , i , " = " , (numero*i))
    return ""

def operaciones_basicas(num1 , num2):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    division = num1 / num2
    
    resultados = (suma,resta,multi,division) # Creo la tupla con los resultados
    print ("suma: ", resultados[0],  " / resta: ", resultados[1], " / multiplicacion: ", resultados[2], " / division: ", resultados[3])
    return ""

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calcular_promedio(a, b, c):
    return (a + b + c) / 3
  

# PROGRAMA PRINCIPAL 
# # Ejercicio 1 
# print(saludo())

# # Ejercicio 2 
# nombre = input("ingrese su nombre: ")
# print(saludar_usuario(nombre))

# # Ejercicio 3
# nombre = input("ingrese su nombre: ")
# apellido = input("ingrese su apellido: ")
# edad = input("ingrese su edad: ")
# provoncia = input("ingrese la pronvincia donde vive: ")
# print(informacion_personal(nombre,apellido,edad,provoncia))

# # Ejercicio 4 
# radio = int(input("ingrese el radio: "))
# print(f"El area del circulo es ", calcular_area_circulo(radio))
# print(f"El perimetro del circulo es: " , calcular_perimetro_circulo(radio))


# # Ejercicio 5 
# segundos = int(input("ingrese la cantidad de segundos que desea saber: "))
# print(segundos, " segundos son equivalentes a: ", segundos_a_horas(segundos), " hora/s.")


# # Ejercicio 6 
# numero = int(input("ingrese un numero: "))
# print(tabla_multiplicar(numero))


# Ejercicio 7 
# num1 = int(input("ingrese un numero: "))
# num2 = int(input("ingrese un numero: "))

# print(operaciones_basicas(num1,num2))


# # Ejercicio 8 
# peso = float(input("ingrese su peso en kilogramos: "))
# altura = float(input("ingrese su altura en metros: "))

# imc = calcular_imc(peso,altura)
# print("Su IMC es: ", imc)


# # Ejercicio 9 
# celcius = float(input("ingrese la temperatura en grados Celsius: "))
# fahrenheit = celsius_a_fahrenheit(celcius)
# print("La temperatura en fahrenheit es: ", fahrenheit) 


# Ejercicio 10 
# num1 = float(input("ingrese el primer numero: "))
# num2 = float(input("ingrese el segundo numero: "))
# num3 = float(input("ingrese el tercer numero: "))

# print("El promedio es: " , calcular_promedio(num1,num2,num3))