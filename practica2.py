
try:
    numero1 = int(input("ingrese primer valor: "))
    numero2 = int(input("ingrese segundo valor: "))
    opereta = input("Ingrese la operacion deseada: ")


    if opereta == "+":
        resultado = numero1 + numero2
        print(f"ESULTADO ENTRE: {numero1} + {numero2} = {resultado}")
    elif opereta == "-":
        resultado = numero1 - numero2
        print(f"ESULTADO ENTRE: {numero1} - {numero2} = {resultado}")
    elif opereta == "*":
        resultado = numero1 * numero2
        print(f"ESULTADO ENTRE: {numero1} * {numero2} = {resultado}")
    elif opereta == "/":    
        if numero2 == 0:
            print("No se puede dividir por cero")
        else:
            resultado = numero1 / numero2
            print(f"RESULTADO ENTRE: {numero1} / {numero2} = {resultado}")
    else:
        print("Operacion no valida")

except ValueError:
    print("Error: Debe ingresar un numero")