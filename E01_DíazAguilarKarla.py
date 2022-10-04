# Karla Díaz Aguilar
# 27/09/2022

# To show the menu ultil user stops
linkedList = []
while True:
    menu = int(input("<<< Menú >>>\n\n¿Qué desea hacer?\n1. Mostrar\n2. Insertar\n3. Eliminar\n4. Salir\n\n"))
    
    if menu == 1:   # Añadir
        noFactura = int(input("Número de factura = \t"))
        importe = int(input("Importe = \t"))
        
        if len(linkedList) == 0:
            print("Por el momento tu lista esta vacia, ingresa un dato por favor\n")
        else:
            for i in range(len(linkedList)):
                print(f"Nodo {i+1} ---> {linkedList[i]}")
            
    elif menu == 2:   # Insert
        linkedList.append(input(f"\nIngresa un dato:\t"))

    elif menu == 3:   # Delete
        linkedList.pop(0)   

    elif menu == 4:   # Exit
        print("| <<< Gracias por usar el programa, hasta pronto! >>> |")
        break