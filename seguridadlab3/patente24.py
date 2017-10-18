from itertools import *
letra="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fichero = open ('patente24.txt', 'w')

letpatentes=[]
numpatentes=[]

#números de patentes posibles
for z in range(0,100):
    for w in range(0,100):
        if(z<10):
            if(w<10):
                numpatentes.append('0'+str(z)+'0'+str(w))
            else:
                numpatentes.append('0'+str(z)+str(w))
        else:
            if(w<10):
                numpatentes.append(str(z)+'0'+str(w))
            else:
                numpatentes.append(str(z)+str(w))
        
    

#combinatorias de letras posibles
for it in combinations_with_replacement(letra,2):
        letpatentes.append(''.join(it))
        

#Patentes completas        
for element in product(letpatentes,numpatentes):
    fichero.write(''.join(element)+"\n")

print("fin")

fichero.close()

