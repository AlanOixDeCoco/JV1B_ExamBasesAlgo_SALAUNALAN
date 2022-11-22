"""
# 1 Affichage de la grille
grid = "1  2  3\n4  5  6\n7  8  9" # les 9 cases du ttt numérotées
print(grid) # on profite des caractères de retour à la ligne '\n'
"""

"""
# 2 Jouer un O ou un X
finished = False # pour savoir si la partie est finie
while(not finished): # tant que la partie n'est pas finie
    print("Placer un 'O' ou un 'X' ?")
    validChoice = False
    while(not validChoice):
        choice = input("Choix : ").capitalize() # toujours prendre la majuscule
        playerMark = "" # le caractère à placer selon le joueur
        if(choice == "X"): # si c'est le joueur 1
            playerMark = "X"
            validChoice = True
        elif(choice == "O"): # si c'est le joueur 2
            playerMark = "O"
            validChoice = True
        else:
            print("Ce n'est pas un choix valide !")

    print("Quel emplacement ?")
    validChoice = False
    while(not validChoice):
        choice = input("Choix : ")
        if(grid.find(choice) == -1): # si case pas dispo (ou pas existante)
            print("Case indisponible !")
        else:
            validChoice = True

    if(choice == '1'):
        grid = grid.replace("1", playerMark)
    elif(choice == '2'):
        grid = grid.replace("2", playerMark)
    elif(choice == '3'):
        grid = grid.replace("3", playerMark)
    elif(choice == '4'):
        grid = grid.replace("4", playerMark)
    elif(choice == '5'):
        grid = grid.replace("5", playerMark)
    elif(choice == '6'):
        grid = grid.replace("6", playerMark)
    elif(choice == '7'):
        grid = grid.replace("7", playerMark)
    elif(choice == '8'):
        grid = grid.replace("8", playerMark)
    elif(choice == '9'):
        grid = grid.replace("9", playerMark)

    print(grid) # affichage de la grille modifiée

    print("Fin de partie ?")
    finished = input("\"Rien\" = continuer : ")
"""

"""
# 3 alignés

# lignes horizontales
if((grid[0] == grid[3] == grid[6]) or (grid[8] == grid[11] == grid[14]) or (grid[16] == grid[19] == grid[22])):
        print("Joueur ", grid[0], " a gagné !")
        finished = True

# lignes verticales
if((grid[0] == grid[8] == grid[16]) or (grid[3] == grid[11] == grid[19]) or (grid[6] == grid[14] == grid[22])):
        print("Joueur ", grid[0], " a gagné !")
        finished = True

# lignes diagonales
if((grid[0] == grid[11] == grid[22]) or (grid[6] == grid[11] == grid[16])):
        print("Joueur ", grid[0], " a gagné !")
        finished = True
"""

"""
# 4 grille complète
    nCrosses = grid.count("X")
    nCircles = grid.count("O")
    if(nCrosses + nCircles == 9): # si il y a 9 cases remplies
        print("Egalité, fin de partie !")
        finished = True
"""

"""
# 5
cf code complet
"""

"""
# 6 Transformer en puissance 4
Pour transformer ce code en puissance 4 il faudrait ajouter des nombres à 
la grille de départ et modifier les conditions de victoire :
    - grille complète = 25 cases (5x5)
    - aligné = comparer sur 4 cases l'alignement
--> Le temps de modification de cet algorithme pousserait à une conception
à l'aide de tableaux et une nouvelle vérification de la victoire.
(La conception de cette approche est disponible dans "testPuissance4.py",
manquent les conditions de victoire)
"""