horario = [    ['Martes y Jueves', '8 am', '406 db', 'Calculo Integral', 'Jairo Lalinde'],
    ['Martes y Jueves', '10 am', '404 db', 'Fisica mecanica', 'Roberto Bohorquez'],
    ['Martes y Jueves', '1 pm', '303 go', 'Programacion orientada a dispositivos mecatronicos', 'David Torres'],
    ['Miercoles', '11 am', '305 db', 'Dibujo de maquinas', 'Elmer Cepeda'],
    ['Miercoles', '1 pm', '204 ps', 'Circuitos Dc', 'Hernan Pineda'],
    ['Viernes', '11 am', '305 db', 'Fundamentos de invetigacion', 'Julian Cortez'],
    ['Viernes', '1 pm', '204 ps', 'Circuitos Dc', 'Hernan Pineda'],
]

materia = input('Ingrese la materia que desea buscar: ')

encontrado = False
for clase in horario:
    if clase[3] == materia:
        dia, hora, salon, profesor = clase[0], clase[1], clase[2], clase[4]
        print(f'La clase de {materia} es el {dia} a las {hora}, en el salón {salon} con el profesor {profesor}.')
        encontrado = True
        break

if not encontrado:
    print(f'Lo siento, la materia {materia} no está en el horario.')

