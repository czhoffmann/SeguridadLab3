from itertools import *
letra="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fichero = open ('patente42.txt', 'w')

letpatentes=[]
numpatentes=[]

#números de patentes posibles
for z in range(0,100):
    if(z<10):
        numpatentes.append('0'+str(z))
    else:
        numpatentes.append(str(z))
   

#combinatorias de letras posibles
for it in combinations_with_replacement(letra,2):
    for item in combinations_with_replacement(letra, 2):
        letpatentes.append(''.join(it)+''.join(item))
        

#Patentes completas
cont=0
for element in product(letpatentes,numpatentes):
    #fichero.write(''.join(element)+"\n")
    cont+=1
print(cont)

print("fin")
#fichero.close()
