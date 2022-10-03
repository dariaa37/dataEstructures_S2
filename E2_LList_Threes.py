# Karla Díaz Aguilar
# 03/10/2022
# Multiplicación matrices

def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:7}'.format(item) for item in row])for row in keanu]) + "\t\n")


# Define Principal Matrix 
A = (
    [1,2,3],
    [4,5,6] 
) 

B = (
    [-1,0],
    [0,1],
    [1,1]
)

# for i in range(2):
#     # Ingresa filas de matriz
#     sizeM = int(input(f"\n<<< NÚMERO DE COLUMNAS {i+1}\t"))
#     noEcuacion = 0

#     while True:
#         noEcuacion += 1     # Guarda ciclo while
#         ecuacion = []       # Guarda valores de la ecuación (solo durante un ciclo)

#         print(f"Ingrega datos de:\nECUACIÓN {noEcuacion}")      # Ingresa los valores de la fila
#         for i in range(sizeM):
#             ecuacion.append(float(input(f"Valor {i+1}:\t")))
#         originalMatrix.append(ecuacion)         # Ingresa la fila (array) a matriz

#         if noEcuacion == sizeM:
#             break

#     print("\nMatriz a resolver:")       # Show Matrix
#     theMatrix(originalMatrix)

# Size variables
filas_A = len(A)    # Cantidad de filas x matriz
colum_A = len(A[0]) # Cantidad de columnas

filas_B = len(B)
colum_B = len(B[0])

if colum_A == filas_B:
    print("Si es posible resolver la multiplicación AxB\n")

    for i in range(filas_A):
        fila = A[i][]
        for j in range(colum_A):
            A[i][j] * B[j][]