from os import system

lista =['Aceptar','Cancelar','Salir','Volver']


def Menu():
    seleccion = 0
    while(seleccion == 0 or seleccion > opcion ):
        opcion = 0
        system("cls")
        for i in lista:
            print(f'{opcion+1}-{i}')
            opcion = opcion+1
        print('Seleccione el numero de opcion')
        try:
            seleccion = int(input())
        except:
            seleccion = 0
    
    system("cls")
    print(f'Usted selecciono la opcion {seleccion} - ',lista[seleccion-1])