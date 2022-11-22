from datetime import datetime
import random

myTable = [0, 4, 1, 3, 8, 0, 7, 9, 3, 2, 10, 4, 3, 2]

print("Tableau initial : ", myTable)

# 1 permutation de deux éléments à partir de leurs indices
temp = myTable[0]
myTable[0] = myTable[1]
myTable[1] = temp

print("Après 1) : ", myTable)

# 2 itération du tri à bulle #############################
for index in range(1, myTable.__len__()): # on commence à 1 car on compare à gauche de l'index
    if(myTable[index-1] > myTable[index]): # si valeur gauche > valeur droite
        # on échange les deux valeurs
        temp = myTable[index-1]
        myTable[index-1] = myTable[index]
        myTable[index] = temp

print("Après 2) : ", myTable)

# 3 tri complet ##########################################
"""
# génération de 1000 valeurs supplémentaires aléatoirement (test performances)
for index in range(0, 1000):
    myTable.append(random.randint(0, 20))
"""

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

# 4 réflexion & optimisation
"""
Le tri à bulles est lent car on vérifie et interchange chaque couple de valeur à chaque itération,
un algorithme par sélection ou insertion permet d'éviter la permutation des valeurs et donc d'économiser
du temps de calcul, en ne déplaçant en fin d'itération que certaines valeurs.
Cela est utile car avec l'algorithme de tri à bulle, même si on peut optimiser légèrement l'algorithme
(ajout d'un booléen sorted ou d'un nombre d'itérations pour modifier l'amplitude des itérations),
les valeurs du début du tableau seront toujours traitées plusieurs fois même si elles sont déjà triées.

Pour connaitre la durée d'exécution du programme on peut utiliser la fonction datetime.now, et comparer
l'heure de début et de fin de traitement (voir exo 3), cependant il faut utiliser un tableau de taille significative.
"""