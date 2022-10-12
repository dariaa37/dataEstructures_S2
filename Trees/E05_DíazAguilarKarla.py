# EJERCICO 5
# DÍAZ AGUILAR KARLA (fila 1)

import locale

locale.setlocale( locale.LC_ALL, '' )

inmuebles = {
        0 : {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
        1 : {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, 
        2 : {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, 
        3 : {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, 
        4 : {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
}

# FUNCIÓN PARA CALUCLAR PRECIO EN ZONA A
def zoneA(meter, rooms, garage, antiquity):
        precio = int((meter*1000 + rooms*5000 + garage*15000) * (1 - (2022 - antiquity)/100))
        return precio

# FUNCIÓN PARA CALUCLAR PRECIO EN ZONA B
def zoneB(meter, rooms, garage, antiquity):
        precio = float((meter*1000 + rooms*5000 + garage*15000) * (1 - (2022 - antiquity)/100) * 1.5)
        return precio

# FUNCIÓN PARA VER POSIBLES INMUEBLES EN FUNCIÓN DEL PRESUPUESTO
def posibleProperty(budget,dictionary):
        print("\n>>> INMUEBLES DISPONIBLES (considerando presupuesto)\n| {:<13} | {:<15} |".format("INMUEBLE", "PRECIO"))
        for i in range(0, len(dictionary)):
                if dictionary[i]["precio"] <= budget:
                        price = locale.currency(dictionary[i]["precio"], grouping = True)
                        print("| {:<13} | {:<15} |".format(f"Propiedad {i+1}", price))
    

def addDictionary(dictionary, function1, funtion2):
        for i in range(len(dictionary)):
                if dictionary[i]["zona"] == "A":         # INMUEBLE EN ZONA A
                        imb = dictionary[i]
                        precio = function1(imb["metros"], imb["habitaciones"], imb["garaje"], imb["año"])
                        # Añadiendo al dicciorario claves y llaves
                        dictionary[i]["precio"] = precio

                elif dictionary[i]["zona"] == "B":         # INMUEBLE EN ZONA B
                        imb = dictionary[i]
                        precio = funtion2(imb["metros"], imb["habitaciones"], imb["garaje"], imb["año"])
                        # Añadiendo al dicciorario claves y llaves
                        dictionary[i]["precio"] = precio

# ENTRADA DATOS
while True:
        menu1 = int(input("······\nBIENVENIDO!\nCONSULTA TU INMUEBLE\nIngresa:\t\n1. Ver inmuebles con tu presupuesto\n2. Terminar"))    

        if menu1 == 1:
                presupuesto = int(input("\nIngresa un presupuesto:\t"))
                # FUNCIONES EN PROCESO
                addDictionary(inmuebles, zoneA, zoneB)
                posibleProperty(presupuesto,inmuebles)

                while True:
                        menu2 = int(input("\nPara más información, ingresa el número de la propiedad o escribe 0 para ingresar otro presupuesto\n| "))
                        
                        if menu2 <= len(inmuebles) and menu2 != 0:
                                print(f"\nINMUEBLE {menu2} | ZONA " + inmuebles[menu2-1]["zona"])
                                print("|{:<20} | {:<15}|".format(f"Año construcción:", inmuebles[menu2-1]["año"]))
                                print("|{:<20} | {:<15}|".format("Extensión (metros):", inmuebles[menu2-1]["metros"]))
                                print("|{:<20} | {:<15}|".format(f"Cant habitaciones:", inmuebles[menu2-1]["habitaciones"]))
                                if inmuebles[menu2-1]["garaje"] == True:
                                        g = "Tiene Garage"
                                elif inmuebles[menu2-1]["garaje"] == False:
                                        g = "Sin Garage"                        
                                print("|{:<20} | {:<15}|".format(f"Año construcción:", g))

                        else:
                                break
        elif menu1 == 2:
                break
# Ciclo para aplicar funciones
# Input para solicitar presupuesto del cliente
# Momstrar inmuebles con precio menor o igual al presupuesto
