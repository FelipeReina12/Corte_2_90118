import random

def maximo(numeros):
    maximo = numeros[0]
    for numero in numeros:
        if numero > maximo:
            maximo = numero
    return maximo

def primos(lista_numeros):
    numeros_primos = []
    for numero in lista_numeros:
        if numero > 1:
            es_primo = True
            for i in range(2, numero):
                if numero % i == 0:
                    es_primo = False
                    break
            if es_primo:
                numeros_primos.append(numero)
    return numeros_primos

numeros_aleatorios = [random.randint(1, 100) for i in range(10)]
print("Números aleatorios generados:", numeros_aleatorios)

maximo = maximo(numeros_aleatorios)
print("El número mayor es:", maximo)

numeros_primos = primos(numeros_aleatorios)
if numeros_primos:
    print(f"Los números primos en la lista son: {numeros_primos}")
else:
    print("No se encontraron números primos en la lista.")