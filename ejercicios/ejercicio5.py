familia = ['Ernets Rombinson','Anna Robinson','Franz Robinson','Jack Robinson']
hijos = ['Franz Robinson','Jack Robinson']

def robinson():
    cantidad = 0

    print('Punto A: ')
    for i in familia:
        if i in hijos:
            cantidad = cantidad+1
    print(f'La cantidad de hijos es: {cantidad}\n')

    print('Punto B: ')
    familia.append(input('Ingrese la moscota de la familia: '))
    for i in familia:
        print(f'{i}')

    print('Punto C: ')
    
