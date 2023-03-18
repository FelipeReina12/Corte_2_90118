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

print("Escoje la operacion matematica que vas a utilizar :")
print("1. Seno")
print("2. Coseno")
print("3. Tangente")
print("4. Exponencial")
print("5. Logartimo natural")

opcion = input("Seleccione una opcion: ")

if opcion == "1":
    print('Escogiste la funcion Seno')
    resultado = calcular_seno()
    print("El seno del número ingresado es:", resultado)
elif opcion == "2":
    print('Escogiste la funcion Coseno')
    resultado = calcular_coseno()
    print("El coseno del número ingresado es:", resultado)
elif opcion == "3":
    print('Escogiste la funcion Tangente')
    resultado = calcular_tangente()
    print("La tangente del número ingresado es:", resultado)
elif opcion == "4":
    print('Escogiste la funcion Exponencial')
    resultado = calcular_exponencial()
    print("La exponencial del número ingresado es:", resultado)
elif opcion == "5":
    print('Escogiste la funcion Logaritmo natural')
    resultado = calcular_logaritmo()
    print("El logaritmo natural del número ingresado es:", resultado)
else:
    print("Opción inválida. Seleccione una opción del 1 al 5.")