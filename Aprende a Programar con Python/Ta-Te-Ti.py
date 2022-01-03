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
    # Se crea una matriz que en realidad es una lista, y con el uso de format se van adjudicando
    # las fichas en el tablero
    print ("| _{}| _{}| _{}|". format (matriz[0], matriz [1], matriz[2]))
    print ()
    print ("| _{}| _{}| _{}|". format (matriz[3], matriz [4], matriz[5]))
    print ()
    print ("| _{}| _{}| _{}|". format (matriz[6], matriz [7], matriz[8]))


def empate(matriz):
#El empate se define cuando ya no existen casilleros vacíos
    empate = True
    i = 0
    while (empate == True and i<9):
        # se crea un indice que reccorre la lista y si encuentra una posición vacía no es empate
        if matriz [i] == " ":
            empate = False
        i = i + 1

    return empate

def victoria(matriz):
    #si ninguno de los siguientes casos está vacío el jugador ganó
    #horizontales
    if (matriz[0]==matriz[1]==matriz[2]!= " " or 
    matriz[3]==matriz[4]==matriz[5]!=" " or 
    matriz[6]==matriz[7]==matriz[8]!=" " or 
    #verticales
    matriz[0]==matriz[3]==matriz[6]!=" " or 
    matriz[1]==matriz[4]==matriz[7]!= " " or 
    matriz[2]== matriz[5]==matriz[8]!= " " or 
    #diagonal
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
            if matriz [casillero-1]== " ": # Si el lugar esta disponible
                matriz[casillero-1]=jugador # en el indice de la lista (menos 1 para reflejar los indices reales) se adjudica la ficha elegida por el jugador
                break
            else:
                print ("Esta posicion no esta disponible")

def movimientos_computadora():
    posiciones=[0,1,2,3,4,5,6,7,8]
    casillero=9
    parar=False

    #Se evalúan chances de ganar

    for i in posiciones: #recorro las posiciones
        copia= list(matriz) #hago una copia de la matriz
        if copia [i]== " ": # Si el indice está vacío
            copia[i]=computadora #La ficha se indica en ese luhar
            if victoria(copia)==True: #Si se logra ganar con ese movimiento
                casillero=i #la ficha se indica en ese indice

    #Se evalúan movimientos para que el jugador humano no gane

    if casillero == 9:
        for j in posiciones: # se recorre la matriz
            copia =list(matriz)
            if copia[j]==" ": # se evalua si el jugador pone la ficha en ese lugar
                copia[j]== jugador
                if victoria(copia)== True: #si el jugador ganaría con ese movimiento
                    casillero=j #la ficha se indica allí
    
    #En caso de que aún no se estén en condiciones de ganar 
    if casillero == 9: #Si el casillero aún es 9
        while (not parar):
            casillero = random.randint(0,8) # Se indica un numero random
            if matriz [casillero]== " ": # Si el casillero está vacío
                parar = True #Y se para
    
    matriz[casillero]= computadora #El casillero se adjudica a la computadora


# PARTIDA

while True:
    matriz=[" "]*9 # se crea una lista vacía de 9 elementos
    os.system("cls") # se borra la pantalla
    jugador,computadora = inicio() # se utiliza la función de inicio para elegir las fichas
    partida = True 
    ganador = 0

    while partida: #Mientas que Partida es true
        ganador = ganador+1 #Por cada movimiento se aumenta 1 para manejar los turnos
        os.system("cls")
        tablero()

        if victoria(matriz): #Se verifica si en el movimiento anterior el usuario ya ganó
            if ganador%2==0: #Si se ganó en un turno impar (ahora es par) es el usuario quien ganó
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
                    
                


            else: #De lo contrario si se ganó en un turno par (ahora es impar) gana la computadora
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
                    

        elif empate(matriz): #Si nadie ganó se evalua el empate (con la funcion definida arriba)
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
                
        #Si no hay empate ni victoria se sigue jugando
        elif ganador%2==0: #La computadora juega en turnos pares
            print ("MI TURNO!")
            time.sleep(2)
            movimientos_computadora()

        else: #El usuario juega en turnos impares (siempre comienza el usuario)
            print ("ES TU TURNO!")
            movimientos_jugador()



            
            

