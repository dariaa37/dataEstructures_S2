# EJERCICO 3
# DÍAZ AGUILAR KARLA

# Contenedores
articles = []
prices = []

def adding(objeto, lista):
    lista.append(objeto)

def prettyList(a,p):
    print("LISTA DE COMPRA")
    print("| {:<15}| {:<10}|".format("ARTICULOS", "PRECIO"))
    total = 0
    for i in range(len(a)):
        total += p[i]
        print("| {:<15}| {:<10}|".format(f"{a[i]}".upper(), f"$ {p[i]}"))
    print("| {:<15}| {:<10}|".format("TOTAL", f"${total}"))
print("BIENVENIDO A LISTA DE COMPRA\nIgresa datos a continuación\nPara dejar de ingresar datos, ingresa (x)")

# CICLO PARA INGRESAR DATOS
while True:
    a = input(f"\n>>> ARTICULO:\t")
    
    if a == "x" or a == "X":
        print("\nINGRESO DE DATOS FINALIZADO\n")
        break
    else:
        p = int(input(f">>> PRECIO:\t"))
        adding(a,articles)
        adding(p,prices)

# Mostrar datos
prettyList(articles,prices)
