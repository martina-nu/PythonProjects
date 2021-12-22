import time
import random
import os


def inicio():
    print("_______________BIENVENID@ A TA-TE-TI_______________")
    time.sleep(1)
    nombre = input("¿Cual es tu nombre?: ")
    while True:
        ficha = input ( nombre + " selecciona tu simbolo X / O: ")
        ficha= ficha.upper()
        if ficha  == "X":
            jugador = "X"
            computadora = "O"
            break
        elif ficha  == "O":
            jugador = "O"
            computadora = "X"
            break
        else: 
            print ("Esa ficha no existe, intentalo de nuevo")
    return (jugador, computadora)

def tablero():
    print ("Este es el tablero. Podes elegir la posicion indicando el numero")
    print ("|1|2|3|")
    print ("|4|5|6|")
    print ("|7|8|9|")
    print ("Empieza la partida. Suerte.")
    print ()
    print ()
    print ("| _{}| _{}| _{}|". format (matriz[0], matriz [1], matriz[2]))
    print ()
    print ("| _{}| _{}| _{}|". format (matriz[3], matriz [4], matriz[5]))
    print ()
    print ("| _{}| _{}| _{}|". format (matriz[6], matriz [7], matriz[8]))


def empate(matriz):
    empate = True
    i = 0
    while (empate == True and i<9):
        if matriz [i] == " ":
            empate = False
        i = i + 1

    return empate

def victoria(matriz):
    if (matriz[0]==matriz[1]==matriz[2]!= " " or 
    matriz[3]==matriz[4]==matriz[5]!=" " or 
    matriz[6]==matriz[7]==matriz[8]!=" " or 
    matriz[0]==matriz[3]==matriz[6]!=" " or 
    matriz[1]==matriz[4]==matriz[7]!= " " or 
    matriz[2]== matriz[5]==matriz[8]!= " " or 
    matriz[0]==matriz[4]==matriz[8]!= " " or 
    matriz[2]==matriz[4]==matriz[6]!= " "):
        return True
    else:
        return False

def movimientos_jugador():
    while True:
        posiciones=[1,2,3,4,5,6,7,8,9]
        casillero = int(input("Elegi una posicion disponible: "))
        if casillero not in posiciones:
            print ("Esta posicion no esta disponible")
        else:
            if matriz [casillero-1]== " ":
                matriz[casillero-1]=jugador
                break
            else:
                print ("Esta posicion no esta disponible")

def movimientos_computadora():
    posiciones=[0,1,2,3,4,5,6,7,8]
    casillero=9
    parar=False

    for i in posiciones:
        copia= list(matriz)
        if copia [i]== " ":
            copia[i]=computadora
            if victoria(copia)==True:
                casillero=i

    if casillero == 9:
        for j in posiciones:
            copia =list(matriz)
            if copia[j]==" ":
                copia[j]== jugador
                if victoria(copia)== True:
                    casillero=j
    
    if casillero == 9:
        while (not parar):
            casillero = random.randint(0,8)
            if matriz [casillero]== " ":
                parar = True
    
    matriz[casillero]= computadora

while True:
    matriz=[" "]*10
    os.system("cls")
    jugador,computadora = inicio()
    partida = True
    ganador = 0

    while partida:
        ganador = ganador+1
        os.system("cls")
        tablero()

        if victoria(matriz):
            if ganador%2==0:
                print ("GANASTE!!!!!!!")
                print ("FIN DEL JUEGO")
                opcion = input("Jugar de nuevo? S/N: ")
                opcion = opcion.upper()
                if opcion == "S":
                    print ("OK! Reiniciando el juego....")
                    time.sleep(5)
                    partida = False
                else:
                    print ("Ok. Gracias por jugar")
                    time.sleep(60)
                    
                


            else:
                print ("PERDISTE!!!!!!!")
                print ("FIN DEL JUEGO")
                opcion = input("Jugar de nuevo? S/N: ")
                opcion = opcion.upper()
                if opcion == "S":
                    print ("OK! Reiniciando el juego....")
                    time.sleep(5)
                    partida = False
                else:
                    print ("Ok. Gracias por jugar")
                    time.sleep(60)
                    

        elif empate(matriz):
            print ("EMPATE!!!!!!!")
            print ("FIN DEL JUEGO")
            opcion = input("Jugar de nuevo? S/N: ")
            opcion = opcion.upper()
            if opcion == "S":
                print ("OK! Reiniciando el juego....")
                time.sleep(5)
                partida = False
            else:
                print ("Ok. Gracias por jugar")
                time.sleep(60)
                
        elif ganador%2==0:
            print ("MI TURNO!")
            time.sleep(2)
            movimientos_computadora()

        else:
            print ("ES TU TURNO!")
            movimientos_jugador()



            
            

