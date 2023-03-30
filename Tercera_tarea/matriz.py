import random

matriz = [[random.randint(1,100) for j in range(10)] for i in range(5)]

for i in range(5):
    for j in range(10):
        print(matriz[i][j], end=' ')
    print()

num_max = matriz[0][0]
num_min = matriz[0][0]
pos_max = (0, 0)
pos_min = (0, 0)

for i in range(5):
    for j in range(10):
        if matriz[i][j] > num_max:
            num_max = matriz[i][j]
            pos_max = (i, j)
        elif matriz[i][j] < num_min:
            num_min = matriz[i][j]
            pos_min = (i, j)

# Ordenar la matriz de menor a mayor
for fila in matriz:
    fila.sort()

print('\nMatriz ordenada de menor a mayor: ')
for i in range(5):
    for j in range(10):
        print(matriz[i][j], end=' ')
    print()

print(f'\nEl numero mayor de la matriz es: {num_max} y se encuentra en la posicion: {pos_max}')
print(f'El numero menor de la matriz es: {num_min} y se encuentra en la posicion: {pos_min}')

