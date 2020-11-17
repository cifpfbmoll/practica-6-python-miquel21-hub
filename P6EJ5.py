#PRÁCTICA 6 EJERCICIO 5
#Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. Para acabar de escribir los números, /
#escribe un número que no sea mayor que el anterior. El programa termina escribiendo la lista de números.
print("Introduce números cada vez más grandes y para acabar ponga uno menor que el anterior")
número_1=int(input("Introduce un número"))
número_2=int(input("Introduce otro número"))
lista_numeros=[número_1]
while número_1<número_2:
    número_1=número_2
    lista_numeros.append(número_1)
    número_2=int(input("Introduce más números"))
print("Los números que has escrito son:", end=" ")
for i in range (len(lista_numeros)-1):
    print(lista_numeros[i], end=", ")
print((lista_numeros[-1]))

