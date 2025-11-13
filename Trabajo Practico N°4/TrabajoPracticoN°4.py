import random
# # EJERCICIO 1   
# for i in range (0,101):
#     print(i)


# # EJERCICIO 2
# num = int(input("ingrese un numero: "))
# cant_digitos  = 0 

# if num ==0:
#     cant_digitos= 1
# else:
#     while num > 0:
#         num = num // 10
#         cant_digitos += 1

# print("cantidad de digitos: ", cant_digitos)


# #EJERCICIO 3 
# num1 = int(input("ingrese un numero: "))
# num2 = int(input("ingrese un numero: "))

# acum = 0 
# for i in range (num1+1, num2,1):
#     acum = acum + i

# print(acum)


# # EJERCICIO 4 
# num = 1
# acum = 0 
# while num != 0:
#     num = int(input("ingrese un numero: "))
#     acum = acum + num 

# print(acum)


# #EJERCICIO 5 
# numero_random = random.randint(0,9)
# cant_intentos = 0

# usuario = int(input("adivine el numero: "))
# while usuario != numero_random:
#     print(numero_random)
#     cant_intentos += 1
#     usuario = int(input("adivine el numero: "))


# print("ADIVINASTE, el numero era",numero_random, "hiciste", cant_intentos, "intento/s para lograrlo")


# # EJERCICIO 6 
# for i in range (0,101,2):
#     if i % 2 == 0: 
#         print(i)

# EJERCICIO 7 
# num = int(input("ingrese un numero: "))

# acum = 0 
# for i in range (0, num + 1):
#     acum += i 
    
# print (acum) 

# EJERCICIO 8 
# cant_numeros = 0
# pares = 0 
# inpares = 0 
# negativos = 0 
# positivos = 0 


# while cant_numeros < 3:
#     num = int(input("ingrese un numero: "))
#     cant_numeros += 1 
    
#     if num >= 0: 
#         positivos += 1
#     else: 
#         negativos += 1 
    
#     if num % 2 == 0:
#         pares += 1 
#     else: 
#         inpares += 1 
        

# print ("Numeros pares ingresados = ", pares)
# print ("Numeros inpares ingresados = ", inpares)
# print ("Numeros positivos ingresados = ", positivos)
# print ("Numeros negativos ingresados = ", negativos)
    

# EJERCICIO 9 
# cant_numeros = 0
# acum = 0 

# while cant_numeros < 100:
#     num = int(input("ingrese un numero: "))
#     acum += num 
#     cant_numeros += 1 

# final = acum / cant_numeros + 1
# print("promedio de los 100 nuemeros: ",final)


# EJERCICIO 10 
# num = int(input("ingrese un numero: "))
# numero_como_string= str(num)
# ultimo = str(num)[-1]
# nuevo_numero = ultimo + numero_como_string[:-1]

# print(nuevo_numero)


