import random

def aleatorio():
    num = random.randint(100, 120)
    while num in [110, 115, 119]:
        num = random.randint(100, 120)
    return num

def agrup():
    num_list = []
    for i in range(10):
        if i % 2 == 0:
            num = aleatorio()
            while num % 2 != 0:
                num = aleatorio()
        else:
            num = aleatorio()
            while num % 2 == 0:
                num = aleatorio()
        num_list.append(num)
    return num_list

# def agrup():
#     for i in range(10):
#         if i % 2 == 0:
#             num = aleatorio()
#             while num % 2 != 0:
#                 num = aleatorio()
#         else:
#             num = aleatorio()
#             while num % 2 == 0:
#                 num = aleatorio()
#         print(num)

# Inicialmente tenia la funcion de la manera que esta comentada
# me arrojaba el resultado de los numeros aleatorios en orden empezando por par
# pero al final mostraba un None,
# La solucion que encontre fue utilizar listas y almacenarlas en estas.