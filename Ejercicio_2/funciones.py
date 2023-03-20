import math

def calcular_seno():
    num = int(input("Ingrese un número para calcular su seno: "))
    seno = math.sin(num)
    return seno

def calcular_coseno():
    num = float(input("Ingrese un número para calcular su coseno: "))
    coseno = math.cos(num)
    return coseno

def calcular_tangente():
    num = float(input("Ingrese un número para calcular su tangente: "))
    tangente = math.tan(num)
    return tangente

def calcular_exponencial():
    num = float(input("Ingrese un número para calcular su exponencial: "))
    exponencial = math.exp(num)
    return exponencial

def calcular_logaritmo():
    num = float(input("Ingrese un número para calcular su logaritmo natural: "))
    logaritmo = math.log(num)
    return logaritmo