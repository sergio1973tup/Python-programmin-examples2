ages = [19,22,19,24,20,25,26,24,25,24]
newList = []

def alumnos():
    ages.sort()
    print('Punto A:')
    print(f'Las edades ordenasdas son: {set(ages)}, la menor: {ages[0]} y la mayor: {ages[len(ages)-1]}\n')

    ages.sort()
    ages.append(ages[0]-1)
    ages.sort()
    mayor = ages[len(ages)-1]+1
    ages.append(mayor)
    print('Punto B:')
    newList = set(ages)
    print(f'{newList} \n')

    print('Punto C: ')
    ages.insert(2, int(input('ingrese una edad: ')))
    
    print(f'{ages} \n')

    print('Punto D:')
    prom = 0
    for i in set(ages):
        prom = prom + i
    
    print(f'El promodio de edad es: {prom/(len(set(ages)))}\n')

    print('Punto E:')
    ages.sort()
    print(f'El rango de edades es de: {ages[0]} a {ages[len(ages)-1]}')