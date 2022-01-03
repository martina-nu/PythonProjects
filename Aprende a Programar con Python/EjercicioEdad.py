import datetime

edadUsuario = int(input("Ingresa tu edad:  "))

def CalcularEdad ():

    anoActual = datetime.date.today().year
    tiempo = 100 - edadUsuario
    ano100 = anoActual + tiempo

    print ("Cumplirás 100 en el año " , ano100)



while True:
    if edadUsuario != 0:
        CalcularEdad()
        break
    
    else:
        print("Edad incorrecta. Ingresar de nuevo. ")
        edadUsuario = int(input("Ingresa tu edad:  "))
            