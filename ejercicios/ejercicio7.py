from os import system

estudiante = ['Nombre','Apellido','Genero','Edad','Habilidades']
diccionario = {}
estudiantes = []

def cargaEstudiantes():
    cantidad = int(input('cuantos estudiantes desea cargar?: '))
    system("cls")
    for i in range(0,cantidad):
        diccionario = {i: (input(f'Ingrese {i}: ')) for i in estudiante}
        estudiantes.append(diccionario)
        system("cls")

    for i in estudiantes:
        for j in i:
            print(f'{j} : {i[j]}')
        print('\n')

    print('Punto A:')
    print(f'La longitud del diccionario es: {len(estudiante)}')