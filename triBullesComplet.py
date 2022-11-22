import random
from datetime import datetime

myTable = []

# génération de 1000 valeurs supplémentaires aléatoirement (test performances)
for index in range(0, 1000):
    myTable.append(random.randint(0, 20))

# Début test performances
debut = datetime.now()

# Algorithme de tri à bulles
sorted = False
iterations = 0
while(not sorted):
    sorted = True # on considère trié tant que pas eu un seul tri par itération
    for index in range(1, myTable.__len__()-iterations): # on commence à 1 car on compare à gauche de l'index, on ne compare pas la dernière valeur car forcément la plus grande
        if(myTable[index-1] > myTable[index]): # si valeur gauche > valeur droite
            # on échange les deux valeurs
            temp = myTable[index-1]
            myTable[index-1] = myTable[index]
            myTable[index] = temp
            sorted = False # si il y a eu tri, on recommencera une itération
    iterations+=1 # fin de cette itération

# Stop test performances
fin = datetime.now()
duree = fin - debut

print("Après 3) : ", myTable)
print("Temps de traitement 3) : ", duree)