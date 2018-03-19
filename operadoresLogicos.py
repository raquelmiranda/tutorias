#metodo que imprima si un numero es par, ademas si es negativo o positi\


def parPositivoNegativo(num):
    if(( num%2==0) and (num>0)):
        print("El numero es par y es positivo")
    elif((num%2==0)and (num<0)):
        print("El numero es par y es negativo")
    elif(not(num%2==0)and (num<0)):
        print("El numero es impar y es negativo")
    else:
        print("El numero es impar y es positivo")


def imprimirGenero():
    gen = input("Digite:\n F) Femenino\n M) Masculino\n")

    if((gen=="f") or (gen == "F")):
        print("El genero es Femenino")
    elif ((gen == "m") or (gen == "M")):
        print("El genero es Masculino")
    else:
        print("Opcion Invalida\n\n\n")
    imprimirGenero()



imprimirGenero()

#parPositivoNegativo()