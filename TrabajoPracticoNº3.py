from statistics import mode, median, mean
import random
import datetime


#EJERCICIO 1 
edad_usuario = int(input("ingrese su edad: "))
if edad_usuario >= 18:
    print("Es mayor de edad")


#EJERCICIO 2 
#nota = int(input("ingrese su nota: "))
#if nota >= 6:
#    print("aprobado")
#else: 
#    print("desaprobado")


#EJERCICIO 3 
#numero = int(input("ingrese un numero: "))
#if numero % 2 == 0:
#    print("su numero es par")
#else: 
#    print("por favor, ingrese un numero par")


#EJERCICIO 4 
#edad= int(input("ingrese su edad: "))
#if edad < 12:
#    print ("niño")
#elif edad >= 12 and edad <18:
#    print ("adolescente")
#elif edad >= 18 and edad < 30:
#    print ("adulto joven")
#elif edad >= 30:
#    print ("adulto")


#EJERICIO 5
#contraseña = input("defina su contraseña: ")

#if len(contraseña) <= 8 and len(contraseña) >= 14:
#    print ("ha ingresado una contraseña correcta")
#else:
#    print ("por favor, ingrese una contraseña entre 4 y 8 caracteres")

# moda (mode), la mediana (median) y la media (mean)

#EJERCICIO 6
#numeros_random = [random.randint(1,100)for i in range (5)]
#print(numeros_random)

#moda = mode(numeros_random)
#mediana = median(numeros_random)
#media = mean(numeros_random)

#if media == mediana and mediana == moda:
#    print ("sin sesgo")
#elif media > mediana and mediana > moda:
#    print("sesgo positivo")
#elif media < mediana and mediana < moda:
#    print("sesgo negativo")
#else:
#    print("esta lista no entra en ningun parametro estadistico")


#EJERCICIO7 
#frase = input("ingrese una frase o palabra: ").lower()
#if frase[len(frase) -1] == "a" or frase[len(frase) -1] == "e" or frase[len(frase)-1] == "i" or frase[len(frase)-1] == "o" or frase[len(frase)-1] == "u":
#    print(frase,"!")
#else: 
#    print(frase)


#EJERCICIO 8
#nombre = input("ingrse su nombre: ")
#print("seleccione la opcion 1 si desea que su nombre este todo en mayusculas \nseleccione la opcion 2 si desea que su nombre este escrito en minuscula \nseleccione la opcion 3 si desea que la primer letra de su nombre este en mayuscula y el resto en minuscula.")
#opcion = int(input("seleccione una opcion: "))

#if (opcion != 1 and opcion != 2 and opcion != 3):
#    print("ingrese una opcion correcta!")
#elif opcion == 1:
#    print(nombre.upper())
#elif opcion == 2:
#    print(nombre.lower())
#else:
#    print(nombre.title())


#EJERCICIO 9 
#magnitud = int(input("ingrese la magnitud del terremoto: "))

#if magnitud <3:
#    print("muy leve (imperceptible)")
#elif magnitud >= 3 and magnitud <4:
#    print("leve (ligeramente perceptible)")
#elif magnitud >= 4 and magnitud <5:
#    print("Moderado (sentido por personas, pero generalmente no causa daños)")
#elif magnitud >= 5 and magnitud <6:
#    print("Fuerte (puede causar daños en estructuras débiles)")
#elif magnitud >=6 and magnitud <7:
#    print("Muy Fuerte (puede causar daños significativos)")
#elif magnitud >= 7:
#    print("Extremo (puede causar graves daños a gran escala)")



#EJERCICIO 10 
#hemisferio = input("ingrese en que hemisferio se encuentraN (norte) / S (sur): ").lower()
#dia = int(input("dia: "))
#mes = int(input("mes: "))
#anio = int(input("año: "))

#if hemisferio == "n" or hemisferio == "norte":
#    if (mes == 12 and dia <= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
#        print ("invierno")  

#    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
#        print ("primavera")

#    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
#        print ("verano")
  
#    elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
#        print ("otoño")

#elif hemisferio == "s" or hemisferio == "sur":
#    if (mes == 12 and dia <= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
#        print ("verano") 

#    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
#        print ("otoño")

#    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
#        print ("iniverno")

#    elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
#        print ("primavera")
    