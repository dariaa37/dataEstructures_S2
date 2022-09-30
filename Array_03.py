array = []
cant = 6
n_search = 0
thereIsNot = 0
index = 0
repeat = 0

indexes = []

for i in range(cant):
    array.append(int(input(f"Número {i+1}:\t")))

n_search = int(input("\n¿Qué número deseas buscar?\t"))

for i in range(cant):
    if array[i] == n_search:
        index += i
        repeat += 1
        indexes.append(array)

    else:
        thereIsNot += 1

if thereIsNot != cant:
    print(f"El valor ingresado {n_search} se encuenta en la posición {indexes}")

else: print("El numero ingresado no se encuentra ")