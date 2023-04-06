from os import system
import random
def aleatorio():
    aleatorio = random.randint(0,10)

    for i in range(0,3):
        print(f'Intento {i+1}')
        numero = int(input('Intente adivinar el numero, ingrese su eleccion:'))
        if(numero == aleatorio):
            system('cls')
            print('felicitaciones adivino!!')
            break
        else:
            system('cls')
            print('no acerto')