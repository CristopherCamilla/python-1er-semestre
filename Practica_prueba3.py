import numpy as np
import os
nombre=list();rut=list();telefono=list();banco=list();asiento=list()
pasajero=[nombre,rut,telefono,banco,asiento]
a=np.array(range(1,43),dtype='str')

def ingreso_pasajero():
    nom=input('Ingrese nombre Pasajero')
    ru=input('Ingrese Rut Pasajero')
    tel=input('Ingrese Telefono Pasajero')
    ban=input('Ingrese nombre Pasajero')
    nombre.append(nom);rut.append(ru);telefono.append(tel)


def ver_asientos():
    c=1
    for i in range(len(a)):
        print(f'|{a[i].center(5)}',end='')
        if c==6:
            c=0
            print('')
        c=c+1
        
def comprar_asientos():
    ver_asientos()
    num=input('Ingrese numero de asiento: ')
    asiento.append(num)
    if num in a:
        i=int(num)-1
        a[i]='X'
    else:
        print('Asiento ocupado o inexistente')
    
    

def menu():
    '''os.system('cls')'''
    os.system('clear')
    print('MENU')
    print('1- VER ASIENTOS')
    print('2- Comprar Asientos')
    print('3- Anular Vuelo')
    print('4- Modificar dato pasajero')
    print('5- Salir')
    return input('Ingrese una Opcion: ')

while True:
    ops=menu()
    if ops=='1':
        ver_asientos()
    if ops=='2':
        comprar_asientos()
    input('...')

