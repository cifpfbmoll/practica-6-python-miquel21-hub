#PRÁCTICA 6 EJERCICIO 3
#Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que /
#no esté entre 0 y 10. El programa termina escribiendo la lista de notas.
notas=float(input("Introduzca las notas y para terminar ponga una nota que no este entre 0 o 10 \n"))
lista_notas=[]
while notas>0 and notas<10:
    lista_notas+=[notas]
    notas=float(input("Introduca mas notas\n"))
print ("Las notas son:",lista_notas)
