# EJERCICIO 1
# Pedí al usuario que ingrese dos números (usá input())
# Convertilos a enteros y sumalos.
# Mostrá el resultado con un print().
"""
numero1 = int(input("Ingrese primer valor: "))
numero2 = int(input("Ingrese segundo valor: "))

print(f"Resultado: {numero1 + numero2}")

"""

# EJERCICIO 2
# Pedí al usuario un número y decile si es par o impar.
"""
numero = int(input("Ingresa un numero: "))

if numero % 2 == 0:
    print(f"El numero: {numero} es PAR !")
else:
    print(f"El numero {numero} es IMPAR!")
"""

# EJERCICIO 3
# Creá una lista vacía.
# Pedí al usuario 3 tareas (usá input()) y agregalas a la lista.
# Al final, mostrá la lista completa.
"""

lista = []

palabra1 = str(input("Ingresa primer palabras: "))
lista.append(palabra1)
palabra2 = str(input("Ingresa segunda palabras: "))
lista.append(palabra2)
palabra3 = str(input("Ingresa tercera palabras: "))
lista.append(palabra3)
print(f"Lista completa {lista}")
"""

# EJERCICIO 4
# Escribí una función llamada "multiplicar" que reciba dos números
# y devuelva el resultado de multiplicarlos.
# Probala con dos valores que vos elijas.
"""
def multiplicar():
    numero1 = int(input("Ingresa valor 1: "))
    numero2 = int(input("Ingresa valor 2: "))
    print(f"El resultado de {numero1} POR {numero2} es: {numero1*numero2}")
multiplicar()
"""

# Pedí al usuario que ingrese 5 números y guardalos en una lista.
# Mostrá solo los números que sean mayores a 10.

lista =[]

for i in range(5):
    numeros = int(input(f"Ingresá 5 numeros: {i+1}: "))
    numeros.append(numeros)
    print("Números mayores a 10:")
for numero in numeros:
    if numero > 10:
        print(numero)