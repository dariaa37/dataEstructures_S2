# EJERCICO 3
# DÍAZ AGUILAR KARLA

diccionario = {}

print("DICCIONARIO ESPAÑOL-INGLÉS")

# CICLO PARA INGRESAR DATOS
c = 0
while True:
    menu = int(input("\n------\nMenú\n1. Ingresar palabras al diccionario\n2. Consultar palabra\n3. Salir\n|\t"))
    
    if menu == 3:       # SALIR
        print("\n¡Vuelve pronto!")
        break

    if menu == 1:       # Añadir
        print("\n· AÑADIENDO A DICCIONARIO\nIgresa una palabra en español y su respectivo equivalente en inglés\nPara dejar de ingresar datos, escribe (x)")
        while True:
            print(f"\nPALABRA {c+1}")
            español = str(input(f">>> ESPAÑOL:\t"))
            
            if español == "x" or español == "X":
                print("|INGRESO DE DATOS FINALIZADO\n")
                break
            else:
                ingles = str(input(f">>> INGLÉS:\t"))
                # Añadiendo al dicciorario claves y llaves
                diccionario[español] = ingles
                c += 1

    if menu == 2:
        print("\n· CONSULTA EN PROCESO")
        palabra = input("Igresa la palabra en español:\t")
        inDicccionario = palabra in diccionario

        if inDicccionario == False:
            print("La traducción no esta disponible :(")
        
        else:
            print(f"<<{palabra}>> en inglés es:\t{diccionario[palabra]}")
