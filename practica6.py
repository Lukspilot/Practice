"""
Ejercicio: "Cajero automático básico"

Descripción:
Vas a simular un cajero automático muy simple. El usuario tiene una cuenta con un saldo inicial de $1000.
El programa debe permitirle al usuario:
-Consultar el saldo.
-Depositar dinero.
-Retirar dinero.
-Salir del programa.

Requisitos:
Mostrar un menú con las 4 opciones.
Pedir al usuario que ingrese una opción.

Si elige "Depositar", pedir cuánto quiere depositar y sumarlo al saldo.
Si elige "Retirar", pedir cuánto quiere retirar y restarlo al saldo, solo si hay suficiente dinero.
Si elige "Consultar saldo", mostrar el saldo actual.
Repetir el menú hasta que el usuario elija salir.

Extra (si querés subir la dificultad un poquito):
-Validar que no se ingresen valores negativos ni letras.
-Agregar un intento limitado para contraseñas (ej: máximo 3 intentos para entrar al cajero).

"""
import os

saldo = 1000

while True:  # Bucle infinito para repetir el menú
    os.system('clear')  # Limpia la pantalla en cada iteración
    print("A - Consultar saldo \nB - Depositar dinero\nC - Retirar dinero\nD - Salir del programa")
    usuario = input("Ingrese opción para continuar: ").lower()  # Convertir a minúsculas para evitar errores

    if usuario == "a":
        print(f"Su saldo es: {saldo}")
    elif usuario == "b":
        try:
            depositar = float(input("Ingrese valor a depositar: "))
            if depositar > 0:
                saldo += depositar
                print(f"Su nuevo saldo es: {saldo}")
            else:
                print("El valor a depositar debe ser positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif usuario == "c":
        try:
            extraer = float(input("Ingrese valor a retirar: "))
            if extraer > saldo:
                print("No tiene suficiente saldo.")
            elif extraer > 0:
                saldo -= extraer
                print(f"Su nuevo saldo es: {saldo}")
            else:
                print("El valor a retirar debe ser positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif usuario == "d":
        print("Gracias por usar el cajero automático.")
        break  # Salir del bucle
    else:
        print("Opción no válida.")

    input("\nPresione Enter para continuar...")  # Pausa antes de volver al menú
