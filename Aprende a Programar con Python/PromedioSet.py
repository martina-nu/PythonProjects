
setUsuario = set()

opcion = input("Deseas agregar un numero al set? s/n ").lower()

while True:
 
    if opcion == "s":
        numero = int(input("Escribe un numero "))
        setUsuario.add(numero)
        opcion = input("Deseas agregar otro nunmero al set? s/n ").lower()

    elif opcion == "n":
        if len(setUsuario):
        
            largoSet = len(setUsuario)
            promedio = sum(setUsuario)/largoSet

            print(f"El promedio de los elementos en el set es: {promedio}")

            break

        else:
           print("No agregaste ningún numero. No se puede realizar el calculo de promedio")
           break

    else:
        print("Opción incorrecta")
        opcion = input("Deseas agregar un numero al set? s/n ").lower()