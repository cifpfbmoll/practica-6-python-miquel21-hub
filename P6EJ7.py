#Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de los números introducidos supere el límite/
#inicial.El programa termina escribiendo la lista de números.
num_limite=int(input("Introduce el número límite"))
valor=int(input("Introduce valor"))
lista=[valor]
while sum(lista)<=num_limite:
    valor2=int(input("Introduce otro valor"))
    lista.append(valor2)
print(f"El número a superar es {num_limite}. La lista creada es: ", end=" ")
for i in range (len(lista)):
     if i==len(lista)-1:
        print(lista[i], end=" ,")
     else:
        print(lista [i], end=", ")
print(f"ya que la suma de estos números es: {sum(lista)}")


