#PRÁCTICA 6 EJERCICIO 12
#Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar). El programa empieza pidiendo entre qué números/
#está el número a adivinar y luego intenta adivinar de qué número se trata. El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que/
#se ha buscado.
import random
minimo = int (input ( "Valor mínimo:"))
maximo = int (input ( "Valor máximo:"))
while maximo<=minimo:
    maximo = int (input ( "Valor máximo:"))
    maximo=maximo
secreto=random.randint(minimo, maximo)
respuesta=input("Es %d ?: "%(secreto))
while respuesta !="igual":
    while respuesta=="mayor":
        minimo=secreto
        secreto=random.randint(minimo, maximo)
        respuesta=input("Es %d ?: "%(secreto))
    while respuesta=="menor":
        maximo=secreto
        secreto=random.randint(minimo, maximo)
        respuesta=input("Es %d ?: "%(secreto))
print("¡Gracias por jugar!")

