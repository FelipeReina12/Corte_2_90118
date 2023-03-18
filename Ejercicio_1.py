import random

def aleatorio():
    num = random.randint(100, 120)
    while num in [110, 115, 119]:
        num = random.randint(100, 120)
    return num

for i in range(10):
    if i % 2 == 0:
        num = aleatorio()
        while num % 2 != 0:
            num = aleatorio()
    else:
        num = aleatorio()
        while num % 2 == 0:
            num = aleatorio()
    print(num)