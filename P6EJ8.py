#PRÁCTICA 6 EJERCICIO 8
#Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de los números introducidos coincida con\
#el número inicial. El programa termina escribiendo la lista de números.
límite=int(input("Introduce el número límite "))
valor=int(input("Introduce valor "))
lista=[valor]
while valor>límite:
    lista.remove(valor)
    print(valor, "es demasiado grande")
    valor=int(input("Introduce otro valor "))
    valor=valor
    lista.append(valor)
while sum(lista)!=límite:
    valor2=int(input("Introduce otro valor "))
    lista.append(valor2)
    if sum(lista)>límite:
        print("Te has pasado")
        lista.remove(valor2)
    print("prueba con otro número")
print("Correcto! El número a alcanzar es",límite,".", "La lista creada es:", end=" ")
for i in range (len(lista)):
    if i==len(lista)-1:
        print(lista[i])
    else:
        print(lista [i], end=" ")
