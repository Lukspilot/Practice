"""
#importamos librerias a utilizar
import os
from datetime import datetime

#funcion de limpiar consola
def limpiar_consola():
    """
    Limpia la consola en función del sistema operativo.
    """
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)

#ejecutamos funcion para limpiar
limpiar_consola()


#Consigna:

#LOGIN 1.1
#Login basico sin bucles perofunciona

usuario = "lukspilot"
contrasena = "lukspilot@"

user = input("Ingrese usuario: ")
contra = input("Ingrese contraseña: ")

if user == usuario and contra == contrasena:
    print("Sesion Iniciada")
else:
    print("Usuario o contrasña incorrectos, intente nuevamente.")


#LOGIN 1.2
#Aca le sumamos un bucle para que se repita en caso de que el usuario o 
#contraseña sea incorrecto

while True:
    usuario = "lukspilot"
    contrasena = "lukspilot"

    user = input("Ingrese usuario: ")
    contra = input("Ingrese contraseña: ")

    if user == usuario and contra == contrasena:
        print("Sesion Iniciada")
        break
    else:
        print("Usuario o contrasña incorrectos, intente nuevamente.")


#LOGIN 1.3
#Aca agregar numero de intentos (Max 3)
#Cuando pasen los 3 intentos saldra un mensaje de error que diga 
# "Cuenta Bloqueada"

contador = 0
while contador <= 2:
    usuario = "lukspilot"
    contrasena = "lukspilot"

    user = input("Ingrese usuario: ")
    contra = input("Ingrese contraseña: ")

    if user == usuario and contra == contrasena:
        print("Sesion Iniciada")
        break
    else:
        contador = contador + 1
        print("Usuario o contrasña incorrectos")
        continue
if contador >2:
    print("Cuenta Bloqueada")



#LOGIN 1.4
#Aca vamos a pulir un detalle que diga la cantidad de intentos 
# que le quedan al usuario antes de bloquear la cuenta"

intentos = 3
while intentos >0:
    usuario = "lukspilot"
    contrasena = "lukspilot"

    user = input("Ingrese usuario: ")
    contra = input("Ingrese contraseña: ")

    if user == usuario and contra == contrasena:
        print("Sesion Iniciada")
        break
    else:
        intentos -= 1
        print(f'Usuario o contrasña incorrectos, te quedan {intentos} intentos.')

if intentos == 0:
    print("Cuenta Bloqueada")

jercicio: Comprobador de números pares e impares
Crea un programa que permita al usuario ingresar un número y le diga si es par o impar.

Instrucciones:
Solicita al usuario que ingrese un número entero.
Usa el operador módulo (%) para determinar si el número es par o impar.
Muestra el resultado en pantalla.



#Ejercicios:

numero = " "

numero = int(input("Ingrese valor entero: "))
if numero % 2 == 0:
    print(f"El numero {numero} es par!")
else:
    print(f"El numero {numero} es impar!")
"""
