# Ejercicio 1. Árboles
# Díaz Aguilar Karla 

prices = [100,50,40,150,80,250]
percent = [20,20,10,20,10,50]
ivaS =  [16,21,19,15,9,17]

# Funciones
def discount(precio,cantDescuento): # FUNCIÓN 1
    precio -= (cantDescuento/100)*precio
    return precio

def theIVA(precio,cantIVA):         # FUNCIÓN 2
    precio += precio*(cantIVA/100)
    return precio

def carrito(precios, var, funcion, toDo):   # FUNCIÓN 3
    total = 0
    # Formato para imprimir tabla
    print("| {:<10}| {:<9}| {:<10}| {:<10}|".format("NO.PRODU","PRECIO", toDo,"SUBOTAL"))
    # Bucle para realizar operaciones y presentar en pantalla
    for i in range(len(precios)):
        subtotal = funcion(precios[i], var[i])  # Guardo el valor obtenido en la función para tener total
        total += subtotal
        print("| {:<10}| {:<9}| {:<10}| {:<10}|".format(i+1 , f"${precios[i]}", f"{var[i]} %", f"${subtotal}" ))
    print(f">>> PRECIO FINAL DE LA COMPRA (aplicando {toDo}) =\t${total}")


print("APLICANDO DESCUENTO")
carrito(prices, percent, discount,"DESCUENTO")
print("\nAPLICANDO IVA")
carrito(prices, ivaS, theIVA, "IVA")