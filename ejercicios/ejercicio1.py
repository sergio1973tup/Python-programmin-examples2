entre = []
impares = []
primos = []
verdadero = ''

def numeros(num1, num2):
    if(num1<num2)&(num1>0):
        for i in range(num1+1,num2):
            entre.append(i)
            if(i%2) != 0:
                impares.append(i)
           
        print('\n')
        print(f'Punto A: entre {num1}-{num2}: {entre}')
        print(f'Punto B: impares {impares}')

        c = 0
        for j in entre:
            for h in range(2,j):
                if j%h == 0:
                    c = c +1
    
            if(c == 0):
                primos.append(j)
            c = 0

        print(f'Punto C: primos {primos}')
        
        fact = 1
        print('Punto C: ')
        for j in entre:
            for i in range(1,j+1):
                fact = fact * i
            print(f'El factorial de: {j} es: {fact}')
            fact = 1
    else:
        print('el primero de los numeros debe ser menos al segundo')