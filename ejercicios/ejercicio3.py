grupo_a_m = 'abcdefghijkm'
grupo_n_z = 'nopqrstuvwxyz'

def grupo(nombre):
    if(nombre[0] in grupo_a_m):
        print('Pertenece al primer grupo')
    else:
        print('Pertenece al segundo grupo')