import locale


inmuebles = {
        0 : {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
        1 : {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, 
        2 : {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, 
        3 : {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, 
        4 : {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
}

def zonaA(meter, rooms, garage, antiquity):
        if garage == True:
                g = 1
        else:
                g = 0

        precio = int((meter*1000 + rooms*5000 + g*1500) * (1 - (2022 - antiquity)/100))
        return precio

def zonaB(meter, rooms, garage, antiquity):
        if garage == True:
                g = 1
        else:
                g = 0
        precio = float((meter*1000 + rooms*5000 + g*1500) * (1 - (2022 - antiquity)/100) * 1.5)
        return precio

presupuesto = int(input("CONSULTA TU INMUEBLE\n"))

for i in range(len(inmuebles)):
        if inmuebles[i]["zona"] == "A":         # INMUEBLE EN ZONA A
                imb = inmuebles[i]
                print(zonaA(imb["metros"], imb["habitaciones"], imb["garaje"], imb["año"]))

        elif inmuebles[i]["zona"] == "B":         # INMUEBLE EN ZONA B
                imb = inmuebles[i]
                print(zonaB(imb["metros"], imb["habitaciones"], imb["garaje"], imb["año"]))

        

# Ciclo para aplicar funciones
# Input para solicitar presupuesto del cliente
# Momstrar inmuebles con precio menor o igual al presupuesto