companias = {'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}

def companies():
    print('\nPunto A: ')
    print(f'El largo del set es: {len(companias)}')

    print('\nPunto B: ')
    print('En un SET no hay primer elemento')

    print('\nPunto C: ')
    nuevasCompanias = []
    for i in range(0,2):
        nuevasCompanias.append(input('Ingrese una compania: '))
    
    for i in nuevasCompanias:
        companias.add(i)
    print(f'ahora con las nuevas companias: {companias}')

    print('\nPunto D: ')
    print(f'SET actual: {companias}')
    companias.remove('IBM')
    print(f'SET sin IBM: {companias}')
    print('la funcion remove() marca error si intentamos borrar algo que ya no esta discard() no da error')

    print('\nPunto E:')
    print('No se puede porque un SET es inmutable')