def k(n, p):
    if n == 0:
        return 0
    else:
        return k(n-1, p) + (n*p) + p

n = int(input("Ingrese el valor de n: "))
p = int(input("Ingrese el valor de p: "))

resultado = k(n, p)
print(resultado)
