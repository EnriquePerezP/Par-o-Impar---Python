#Juego del par o impar
#Programado por Enrique Perez
#10 de diciembre del 2022


print("En que numero estas pensando? ")
num = int(input("Elige un numero entre 1 al 1000: "))

numeros_impares = list(range(1, 1000, 2))

if(num in numeros_impares):
    print("Tu numero es impar")
elif(num > 1000 or num < 1):
    print("Te pasaste del rango")
else:
    print("Tu numero es par")