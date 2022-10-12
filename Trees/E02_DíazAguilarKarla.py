# Ejerccio 2
# Karla Díaz Aguilar

prices = [100,50,40,150,80,250]

def totalFacture(cantidad, iva = 16):   
    total = 0   # Guardara la suma de los subtotales despues de Aplicar IVA

    print("\n" + f" << FACTURA >> ".center(56,"·"))
    print("| {:<10}| {:<18}| {:<10}| {:<9}|".format("NO.PRODU","CANT (antes IVA)", "IVA %","SUBOTAL"))
    for i in range(len(cantidad)):
        subtotal = cantidad[i] + cantidad[i]*(iva/100)
        print("| {:<10}| {:<18}| {:<10}| {:<9}|".format(i+1,f"$ {cantidad[i]}", f"{iva} %",f"$ {subtotal}"))
        total += subtotal
    
    print(">>> TOTAL FACTURA <<<".center(55," "))
    print(f"| ${total} |".center(55," "))

# Con PARAMETROS COMPLETOS 
totalFacture(prices, 18)     
totalFacture(prices, 14) 

# Sin IVA incluido
totalFacture(prices)
