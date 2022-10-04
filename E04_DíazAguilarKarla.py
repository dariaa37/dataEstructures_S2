# Karla Díaz Aguilar
# 04/10/2022

# Ejercicio 4. Listas y árboles.
# To show the menu ultil user stops
facturas = [
        [],
        []
    ]

while True:
    menu = int(input("<<< Menú >>>\n\n¿Qué desea hacer?\n1. Añadir nueva factura\n2. Pagar una existente\n3. Terminar\n\n"))
    
    if menu == 1:   # Añadir
        print("A continuación, ingresa:\n")
        noFactura = int(input("Número de factura = \t"))
        facturas[0].append(noFactura)
        
        importe = int(input("Importe = \t"))
        facturas[1].append(importe)
        
        if len(facturas) == 0:
            print("Por el momento no tienes ninguna factura\n")
            
    elif menu == 2:   # Pagar
        print(facturas)
        facturaPagada = facturas[0].index(int(input(f"Por favor ingresa el NÚMERO DE FACTURA:\t")))
        facturas[0].pop(facturaPagada)      # Elimina numero de factura
        facturas[1].pop(facturaPagada)      # Elimina Importe de la factura

    elif menu == 3:   # Exit
        print("| <<< Gracias por usar el programa, hasta pronto! >>> |")
        break