# Karla Díaz Aguilar
# 04/10/2022

# Ejercicio 4. Listas y árboles.

# To show the menu ultil user stops
facturas = [
        [],
        []
    ]
cantCobrada = 0
cantPendiente = 0

while True:
    menu = int(input("\n<<< Menú >>>\n\n¿Qué desea hacer?\n1. Añadir nueva factura\n2. Pagar una existente\n3. Terminar\n\n".rjust(20,"·")))

    if menu == 1:   # Añadir
        print("A continuación, ingresa:\n")
        noFactura = int(input("Número de factura = \t"))
        facturas[0].append(noFactura)
        
        importe = float(input("Importe = \t\t"))        
        facturas[1].append(importe)
        cantPendiente += importe      # Variable que almacena importe total
                    
    elif menu == 2:   # Pagar
        if len(facturas[0]) == 0:
            print("Por el momento no tienes ninguna factura\n")
        else:
            print(f"\nFACTURAS EXISTENTES")
            for i in range(len(facturas[0])):
                print(f"NO. FACTURA =\t{facturas[0][i]} | IMPORTE = {facturas[1][i]}")
            facturaPagada = facturas[0].index(int(input(f"\nPor favor ingresa el NÚMERO DE FACTURA: \t")))

            cantCobrada += facturas[1][facturaPagada]        # Registra los pagos realizados
            cantPendiente -= facturas[1][facturaPagada]      # Dinero pendiente por pagar
            facturas[0].pop(facturaPagada)      # Elimina numero de factura
            facturas[1].pop(facturaPagada)      # Elimina Importe de la factura

    elif menu == 3:   # Exit
        print("| <<< Gracias por usar el programa, hasta pronto! >>> |")
        break

    # Despues de operaciones
    print(f"\n| Cantidad cobrada hasta el momento =\t{cantCobrada} |")
    print(f"| Cantidad pendiente por cobrar =\t{cantPendiente} |\n")