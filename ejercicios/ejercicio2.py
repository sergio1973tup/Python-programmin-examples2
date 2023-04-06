vocales = 'aeiou'
cuantas = 0

def vocalesFuncion(frase):
    c = 0
    for i in frase:
        for j in vocales:
            if(i == j):
                c = c+1

    print(f'La frase {frase} tiene: {c} vocales')
