def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:9}'.format(item) for item in row])for row in keanu]) + "\n")

# Matrices
mA = (
    (1,2,3),
    (4,5,6)
)

mB = (
    (-1,0),
    (0,1),
    (1,1)
)

mC = [
    [0,0],
    [0,0]
]

# PROCESO
for row in range(2):
    for colum in range(2):
        cons = 0
        for coef in range(3):
            cons += mA[row][coef] * mB[coef][colum]
        mC[row][colum] = cons

print("\nRESULTADO DE AxB = C")
theMatrix(mC)