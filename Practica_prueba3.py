import numpy as np
import os
nombre=list();rut=list();telefono=list();banco=list();asiento=list()
pasajero=[nombre,rut,telefono,banco,asiento]
a=np.array(range(1,43),dtype='str')

def menu():
    os.system('cls')
    #os.system('clear')
    print('MENU')
    print('1- VER ASIENTOS')
    print('2- Comprar Asientos')
    print('3- Anular Vuelo')
    print('4- Modificar dato pasajero')
    print('5- Salir')
    return input('Ingrese una Opcion: ')

def ingreso_pasajero():
    nom=input('Ingrese nombre Pasajero: ')
    ru=input('Ingrese Rut Pasajero: ')
    tel=input('Ingrese Telefono Pasajero: ')
    print('Ingrese Banco')
    global ban
    ban=input('1-SANTANDER, 2-ESTADO, 3-CHILE, 4-BancoDuoc: ')
    nombre.append(nom);rut.append(ru);telefono.append(tel);banco.append(ban)

def ver_asientos():
    c=1
    for i in range(len(a)):
        print(f'|{a[i].center(5)}',end='')
        if c==6:
            c=0
            print('')
        c=c+1

def tomar_asiento():
    global num
    num=input('Ingrese numero de asiento: ')
    asiento.append(num)
    if num in a:
        i=int(num)-1
        a[i]='X'
    else:
        print('Asiento ocupado o inexistente')

def pagar():
    if num<='30':
        monto=78900
    elif num>'30':
        monto=240000
    if ban=='4':
        dcto='15%'
        final=monto*0.85
    else:
        dcto='0%'
        final=monto
    return print(f'Monto a pagar: {final}, Dcto. por banco: {dcto} ')


def anular():
    asi=input('Indicar el asiento para Anular: ')
    try:
        i=asiento.index(asi)
    except: print('INGRESA ASIENTO VALIDO')

    print(f'nombre: {pasajero[0][i]}, rut: {pasajero[1][i]}, telefono: {pasajero[2][i]}, banco: {pasajero[3][i]}, asiento: {pasajero[4][i]}')
    anu=input('Esta seguro de eliminar: 1=SI , 2=NO: ')

    if anu=='1':
        nombre.pop(i);rut.pop(i);telefono.pop(i);banco.pop(i);asiento.pop(i)
        e=int(asi)-1
        a[e]=asi
        print('Anulación Realizada con Exito¡¡')
    else:
        print('Anulación Rechazada¡¡')

def modificar():
    try:
        asi=input('Indicar el asiento: ')
        ru=input('indicar el Rut: ')
        i=asiento.index(asi)
        r=rut.index(ru)
        if i==r:
            print(f'nombre: {pasajero[0][i]}, rut: {pasajero[1][i]}, telefono: {pasajero[2][i]}, banco: {pasajero[3][i]}, asiento: {pasajero[4][i]}')
            print('')
            print('1- Modificar Nombre')
            print('2- Modificar telefono')
            q=input('ingrese opcion: ')
            if q=='1':
                nnew=input('ingrese nuevo nombre: ')
                nombre[i]=nnew
            elif q=='2':
                tnew=input('ingrese nuevo telefono: ')
                telefono[i]=tnew
            print('Datos modificados correctamente')
        else:
            print('Datos no correspaonden a los registros')
    except: print('Datos no validos')

def comprar_asiento():
    ingreso_pasajero()
    ver_asientos()
    tomar_asiento()
    pagar()
    print(pasajero)


while True:
    ops=menu()
    if ops=='1':
        ver_asientos()
    if ops=='2':
        comprar_asiento()
    if ops=='3':
        anular()
    if ops=='4':
        modificar()
    if ops=='5':
        print('PROGRAMA FINALIZADO......')
        break
    input('...')
