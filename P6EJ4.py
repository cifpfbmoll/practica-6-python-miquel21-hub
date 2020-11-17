#PRÁCTICA 6 EJERCICIO 4
#Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero. El programa termina escribiendo los /
#dos números tal y como se pide:
#--------------Declarar variables
numeros1= 1
numeros2 = 0
#
#--------------Logica
while numeros2<numeros1:
    numeros1=int(input("Introduzca un número"))
    numeros2=int(input("Introduzca otro número mayor que el primero"))
listaNumeros=[numeros1]
listaNumeros.append(numeros2)
print(listaNumeros)
