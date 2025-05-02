while True:
    try:
        numero = int(input("Ingrese un numero: "))
        if numero < 0:
            raise ValueError("El numero no puede ser negativo")
        break
        elif numero <= 0:
            print("Correcto")
    except ValueError:
        print("Error: Debe ingresar un numero entero positivo")