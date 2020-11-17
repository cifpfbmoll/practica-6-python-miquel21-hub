#PRÁCTICA 6 EJERCICIO 11
#Escribir un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario lo ha de adivinar). El programa empieza pidiendo entre qué/
#números está el número a adivinar, se "inventa" un número al azar y luego el usuario va probando valores. El programa va decidiendo si son demasiado grandes o/
#pequeños.
import random
minimo = int (input ( "Valor mínimo:"))
maximo = int (input ( "Valor máximo:"))
while maximo<=minimo:
    maximo = int (input ( "Valor máximo:"))
    maximo=maximo
secreto = random.randint(minimo, maximo)
pruebas2=[]
pruebas=[]
print(f"A ver si adivinas un número entero entre {minimo} y {maximo}.")
numero=int(input("Escribe un numero"))
while numero<secreto:
    print("Demasiado pequeño, vuelve a probar.")
    pruebas2.append(numero)
    numero=int(input("Escribe un numero"))
    pruebas.append(pruebas2)
    pruebas2=[]
while numero>secreto:
    print("Demasiado grande, vuelve a probar.")
    pruebas2.append(numero)
    numero=int(input("Escribe un numero"))
    pruebas.append(pruebas2)
    pruebas2=[]
print("Correcto! Lo has intentado:", end=" ")
print(len(pruebas)+1)



