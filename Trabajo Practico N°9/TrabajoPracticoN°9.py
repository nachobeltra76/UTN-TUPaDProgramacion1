# Punto 1 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("ingrese un numero entero positivo: "))

for i in range(1, numero + 1):
    print(f"factorial de {i} es {factorial(i)}")


# punto 2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
posicion = int(input("Introduce una posición (entero positivo): "))

for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")


# punto 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("ingrese la base: "))
exponente = int(input("ingrese el exponente mayor que 0: "))

resultado = potencia(base, exponente)
print(resultado)


# punto 5 
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("ingrese una una palabra sin espacios ni tildes: ").lower()

if es_palindromo(texto):
    print(f"'{texto}' es un palindramo.")
else:
    print(f"'{texto}' no es un palindromo.")


#punto 6 
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Introduce un número entero positivo: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")


# punto 7 
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel_inferior = int(input("ingrese la cantidad de bloques en el nivel mas bajo: "))
total = contar_bloques(nivel_inferior)
print(f"todos los bloques necesarios: {total}")

# punto 8 
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        coincidencia = 1 if numero % 10 == digito else 0
        return coincidencia + contar_digito(numero // 10, digito)
numero = int(input("ingrese un numero entero positivo: "))
digito = int(input("ingfrese el dígito a contar (0-9): "))

if 0 <= digito <= 9:
    resultado = contar_digito(numero, digito)
    print(f"el digito {digito} aparece {resultado} veces en el numero {numero}.")
else:
    print("el digito debe estar entre 0 y 9.")