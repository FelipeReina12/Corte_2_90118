with open('alimentos.txt', 'r') as file:
    dict = {}
    for line in file:
        if len(line.strip().split(',')) >= 3:
            codigo, descripcion, tarifa = line.strip().split(',')[-3:]
            dict[codigo] = (descripcion, tarifa)

print(dict)

while True:
    codigo_producto = input("Ingrese el código del producto (o escriba 'salir' para terminar): ")
    if codigo_producto.lower() == 'salir':
        break
    elif not codigo_producto:
        print("Debe ingresar un código de producto")
        continue
    
    valor_neto = float(input("Ingrese el valor neto del producto: "))

    tarifa_iva = float(dict[codigo_producto][1])
    valor_iva = valor_neto * 0.19
    valor_base = valor_neto / (1 + tarifa_iva) + valor_iva

    print(f"El valor del IVA correspondiente (19%) es: {valor_iva:.2f}")
    print(f"El valor base del producto es: {valor_base:.2f}")
    print()

print("Programa terminado")
