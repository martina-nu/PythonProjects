import random

print ("")
print ("************* BIENVENID@S A DADOS *************")
print ("")

#Funcion para tirar los dados

def tirarDados():
    dado1 = random.choice([1,2,3,4,5,6])       
    dado2 = random.choice([1,2,3,4,5,6])  
    print ("_________RESULTADOS_________")
    print ("")
    print ("El valor del dado 1 es:" , dado1)
    print ("El valor del dado 2 es:" , dado2)
    print ("La suma de los dos dados es: " , dado1 + dado2)
    print ("")
    print ("")

opcion = input("Deseas tirar los dados? s/n: ").lower()
print ("")

while True:

    if opcion =="s": #Si la opcion ingresada es "s" se tiran los dados
        tirarDados()
        opcion = input("Volver a tirar los dados? s/n: ").lower() #Opcion para volver a tirar los dados o salir
        print ("")

        
    elif opcion == "n": #Si la opcion ingresada es n se termina la ejecucion
        print ("")
        print ("")
        print ("************* GRACIAS POR UTILIZAR DADOS, HASTA LA PRÓXIMA *************")
        print ("")
        print ("")
        break

    else: # En caso de que la opcion ingresada no sea valida se puede volver a ingresar
        opcion = input("Opcion incorrecta. Intentalo de nuevo. Deseas tirar los dados? s/n: ").lower()

        

