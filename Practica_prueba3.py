import numpy as np
import os
a=np.array(range(1,43),dtype='str')

def ver_asientos():
    c=1
    for i in range(len(a)):
        print(f'|{a[i].center(5)}',end='')
        if c==6:
            c=0
            print('')
        c=c+1
def comprar_asientos():
    num=input('ingrese numero de asiento')
    if num in a:
        i=int(num)-1
        a[i]='X'
    else:
        print('asiento ocupado o inexistente')

def menu():
    os.system('cls')
    print('MENU')
    print('1- VER ASIENTOS')
    print('2- Comprar Asientos')
    print('3- Anular Vuelo')
    print('4- Modificar dato pasajero')
    print('5- Salir')
    return input('Ingrese una Opcion: ')

while True:
    ops
    if 
