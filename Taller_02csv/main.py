import pandas as pd
import csv

# Leer el archivo CSV con la libreria Pandas para organizarlo
df = pd.read_csv('data.csv')

# Ordena el DataFrame por la columna "Country" en orden alfabético ascendente
df_ordenado = df.sort_values('Country', ascending=True)

# Guarda el DataFrame ordenado en un archivo CSV de salida
df_ordenado.to_csv('data_format_ordenado.csv', index=False)

paises = {}
# Recorrer el archivo CSV y agregar cada país al diccionario
with open('data_format_ordenado.csv') as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)  # saltar la primera fila (encabezados)
    for fila in lector_csv:
        pais = fila[4]
        if pais not in paises:
            paises[pais] = []
        paises[pais].append(fila)

# Imprimir la lista de países numerados
print("Lista de países:")
for i, pais in enumerate(paises.keys()):
    print(f"{i+1}. {pais}")
num_pais = int(input("\nIngrese el número del país que desea visualizar: "))

pais_seleccionado = list(paises.keys())[num_pais-1]
print(f"\nUsted seleccionó el país: {pais_seleccionado}")

empresas = []
with open('data_format_ordenado.csv') as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)  # saltar la primera fila (encabezados)
    for fila in lector_csv:
        pais = fila[4]
        if pais == pais_seleccionado:
            empresas.append(fila)

# Encontrar la empresa con más empleados en el país seleccionado
mayor_empresa = None
mayor_empleados = 0
for empresa in empresas:
    num_empleados = int(empresa[8])
    if num_empleados > mayor_empleados:
        mayor_empleados = num_empleados
        mayor_empresa = empresa

print(f"\nLa empresa con más empleados en {pais_seleccionado} es {mayor_empresa[2]}")
print(f"Sitio web: {mayor_empresa[3]}")
print(f"Descripción: {mayor_empresa[5]}")
print(f"Fundación: {mayor_empresa[6]}")
print(f"Industria: {mayor_empresa[7]}")
print(f"Empleados: {mayor_empleados}")

menor_empresa = None
menor_empleados = float('inf')
for empresa in empresas:
    num_empleados = int(empresa[8])
    if num_empleados < menor_empleados:
        menor_empleados = num_empleados
        menor_empresa = empresa

print(f"\nLa empresa con menos empleados en {pais_seleccionado} es {menor_empresa[2]} ")
print(f"Sitio web: {menor_empresa[3]}")
print(f"Descripción: {menor_empresa[5]}")
print(f"Fundación: {menor_empresa[6]}")
print(f"Industria: {menor_empresa[7]}")
print(f"Empleados {menor_empleados}")

total_empleados = 0
num_empresas = len(empresas)
for empresa in empresas:
    num_empleados = int(empresa[8])
    total_empleados += num_empleados
promedio_empleados = total_empleados / num_empresas

print(f"\nEl promedio de empleados en {pais_seleccionado} es {promedio_empleados:.2f}.")

num_empresas = len(empresas)

print(f"\nCantidad de empresas en {pais_seleccionado}: {num_empresas}")
