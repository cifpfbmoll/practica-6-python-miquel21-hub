#PRÁCTICA 6 EJERCICIO 1
#Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, \
#simplemente pulsa Enter. El programa termina escribiendo la lista de palabras.
print("Escriba sus palabras y cuando termine simplemente dale al enter")
palabras=str(input())
lista_palabras=[]
while palabras!="":
    lista_palabras+=[palabras]
    print("Introduzca más palabras")
    palabras=str(input())
print (lista_palabras)


