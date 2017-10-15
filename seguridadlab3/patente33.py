from itertools import *
letra="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fichero = open ('patente33.txt', 'w')

letpatentes=[]
numpatentes=[]

#números de patentes posibles
for z in range(100,1000):
    numpatentes.append(str(z))

#combinatorias de letras posibles
for it in combinations_with_replacement(letra,2):
    for item in combinations_with_replacement(letra, 1):
        letpatentes.append(''.join(it)+''.join(item))
        

#Patentes completas        
for element in product(letpatentes,numpatentes):
    fichero.write(''.join(element)+"\n")

print("fin")
fichero.close()

