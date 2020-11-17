#PRÁCTICA 6 EJERCICIO 10
#Escribe un programa que te pida los nombres y notas de alumnos. Si escribes una nota fuera del intervalo de 0 a 10, el programa entenderá que no quieres introducir/
#más notas de este alumno. Si no escribes el nombre, el programa entenderá que no quieres introducir más alumnos. Nota: La lista en la que se guardan los nombres y/
#notas tiene esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc].
curso=[]
sublista=[]
nombre=input("Dame un nombre: ")
while(nombre!=""):
    sublista.append(nombre)
    nota=float(input("Escriba una nota: "))
    while (nota>=0)and(nota<=10):
        sublista.append(nota)
        nota=float(input("Escriba otra nota: "))
    curso.append(sublista)
    sublista=[]
    nombre=input("Dame un nombre: ")
print("Las notas de los alumnos son: ")
for i in range(len(curso)):
    print(curso[i][0],":",end=" ")
    print(curso[i][1],end=" ")
    for j in range(1,len(curso[i])):
        print(" - ",curso[i][j],end=" ")
    print("")
