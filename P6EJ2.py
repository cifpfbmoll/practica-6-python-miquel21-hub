#PRÁCTICA 6 EJERCICIO 2
#Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, simplemente escribe “Salir”. /
#el programa termina escribiendo la lista de números.
números=input("Escriba sus números y cuando termine escriba Salir")
lista_numeros=[]
while números!="Salir":
    lista_numeros+=[números]
    números=input("Introduzca más números")
print (lista_numeros)
