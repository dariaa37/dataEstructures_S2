# Karla Díaz Aguilar
# 05/10/2022

# Ejercicio 5. Listas y árboles.
# DATA BASE
dataBase = {
        0 : [],
        1 :[],
        2 :[],
        3 :[],
        4 :[],
        5 :[]       # VIP
    }


while True:
    datosCliente = ("CLIENTE ID:","NOMBRE:", "DIRECCIÓN:","TELEFONO:","CORREO:")
    menu = int(input("_".ljust(30,"_") +"\nCLIENTS DATA BASE\n¿Qué deseas realizar?\n1. Añadir cliente (Client ID)\n2. Eliminar cliente\n3. Mostrar cliente\n4. Ver todos los clientes\n5. Ver Clientes VIP\n6. Terminar\n<< "))
    
    if menu == 6:   # TERMINA
        print("\n| <<< Gracias por usar el programa, hasta pronto! >>> |")
        break

    elif menu == 1:     # AÑADIR CLIENTE
        print("\nPor favor ingrese los siguientes datos del cliente:")
        for i in range(0,len(datosCliente)):
            datos = input(f"| {datosCliente[i]}\t")
            dataBase[i].append(datos.upper())
            
        preferente = int(input(f"| PREFERENTE |\n1. Estandar\n2. VIP\n| "))
        while True:         # Part especifica para preferente
            if preferente == 1:
                dataBase[5].append(False)
                break
            elif preferente == 2:
                dataBase[5].append(True)
                break
            else:
                print("Ingrese un valor nuevamente")
                break
    
    elif menu == 2:     # ELIMINAR CLIENTE
        while True:
            c = input(f"\nIngresa CLIENTE ID:\t")
            if dataBase[0].count(c) > 0:
                cid = dataBase[0].index(c)
                
                for i in range(len(dataBase)):      # for para eliminar datos del cliente
                    dataBase[i].pop(cid)
                break
            else: print("Cliente ID erroneo, ingrese nuevamente por favor")

    elif menu == 3:     # MOSTRAR UN CLIENTE
        while True:
            c = input(f"\nIngresa CLIENTE ID:\t")
            if dataBase[0].count(c) > 0:
                cid = dataBase[0].index(c)
                for i in range(1,len(datosCliente)):      # for para MOSTRAR datos del cliente
                    print(f"| {datosCliente[i]}\t{dataBase[i][cid]}")
                if dataBase[5][cid] == True:    # Mostrar leyenda en lugar de BOOL
                    preferente = "VIP"
                else: preferente = "Estandar"
                print(f"| PREFERENTE:\t{preferente}") 
                break
            else: print("Cliente ID erroneo, ingrese nuevamente por favor")
    
    elif menu == 4:     # TODOS LOS CLIENTES
        print("\n" + "<< TODOS LOS CLIENTES >>".center(30,"·"))
        for i in range(len(dataBase[0])):
            print(f"| {datosCliente[0]}\t{dataBase[0][i]}\t{datosCliente[1]}\t{dataBase[1][i]}")

    elif menu == 5:     # SOLO VIP
        print("\n" + "<< CLIENTES VIP >>".center(30,"·"))
        for i in range(len(dataBase[5])):
            if dataBase[5][i] == True:
                print(f"| {datosCliente[0]}\t{dataBase[0][i]}\t{datosCliente[1]}\t{dataBase[1][i]}")
            else: print("Por el momento, no hay clientes VIP")
    
