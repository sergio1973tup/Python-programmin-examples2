from os import system

def FunctionInput():
    numero = 0
    while(numero != 'E'):
        try:
            numero = int(input('Ingrese un numero: '))
            print(numero)
            numero = 'E'
            
        except:
            system('cls')
            print('se espera un valor entero, vuelva a intentarlo!! estoy previendo un exepcion')
