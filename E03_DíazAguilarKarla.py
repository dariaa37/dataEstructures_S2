# Karla Díaz Aguilar
# 04/10/2022

# Ejercicio 3. Listas y árboles.
# Hacer un programa que solicite una muestra de números (mínimo 6), 
# separados por comas, los guarde en una tupla y muestre por pantalla su media y desviación típica.

# Presentación para el usuario
from cmath import sqrt

while True:

    print("| MEDIA Y DESVIACIÓN TÍPICA |")
    while True:     # Solicita muestra
        muestraNumeros= str(input("Ingresa una muestra numérica separando números con comas (,)\n"))
        cadena = tuple(muestraNumeros.split(sep=","))
        if len(cadena) >= 6:
            break
        else:
            print("\n<<< Ingresa mínimo 6 números")
    
    # Prceso MEDIA (promedio)
    sum = 0
    for i in range(len(cadena)):
        dato = int(cadena[i])     # Variable para hacer INT un STR
        sum += dato
    media = sum/len(cadena)

    # Prceso DESVIACIÓN TÍPICA
    sum = int(0)
    for i in range(len(cadena)):
        dato = int(cadena[i])     # Variable para hacer INT un STR
        sum += (dato[i] - media)**2
    desviacion = sqrt(sum/len(cadena))

    print(f"\nMEDIA =\t\t\t{media}\nDESVIACIÓN TÍPICA = \t{desviacion}".rjust(20,"-"))

    continuar = input("¿Deseas calcular nuevamente?\n1. Si\n2. No\n")

    if continuar == "2" or continuar == "No" or continuar == "no":
        break
