#PRÁCTICA 6 EJERCICIO 6
#Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios. Para terminar de/
#escribir números, escribe un número que no esté comprendido entre los dos valores iniciales. El programa termina escribiendo la/
#lista de números.
num_1=int(input("Escribe el número mínimo \n"))
num_2=int(input("Escribe el número máximo \n"))
while(num_1>=num_2):
    print("¡Le he pedido un número mayor!")
    num_2=int(input("Escribe el número máximo \n"))
num_3=int(input("Escriba un número intermedio \n"))
lista=[]
while num_3<num_2 and num_3>num_1:
    lista.append(num_3)
    num_3=int(input("Escriba otro número intermedio \n"))
    num_3=num_3
print("Los números intermedios de su lista son:", end=" ")
for i in range (len(lista)):
    if i==len(lista)-1:
        print(lista[i])
    else:
        print(lista [i], end=", ")