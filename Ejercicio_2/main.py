import funciones

print("Escoje la operacion matematica que vas a utilizar :")
print("1. Seno")
print("2. Coseno")
print("3. Tangente")
print("4. Exponencial")
print("5. Logartimo natural")

opcion = input("Seleccione una opcion: ")

if opcion == '1':
    print('Haz escogido la funcion seno')
    if __name__ == '__main__':
        seno = funciones.calcular_seno()
        print('El seno es: ', seno)
        print(funciones.num)

elif opcion == '2':
    print('Haz escogido la funcion coseno')
    if __name__ == '__main__':
        coseno = funciones.calcular_coseno()
        print('El coseno es: ', coseno)

elif opcion == '3':
    if __name__ == '__main__':
        print('Haz escogido la funcion tangente')
        tangente = funciones.calcular_tangente()
        print('La tangente es: ', tangente)

elif opcion == '4':
    if __name__ == '__main__':
        print('Haz escogido la funcion exponencial')
        exponencial = funciones.calcular_exponencial()
        print('La exponencial es: ', exponencial)

elif opcion == '5':
    if __name__ == '__main__':
        print('Haz esogido la funciion logaritmo nautural')
        logaritmo = funciones.calcular_logaritmo()
        print('El logaritmo es: ', logaritmo)