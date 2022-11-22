grid = "1  2  3\n4  5  6\n7  8  9" # les 9 cases du ttt numérotées
print(grid) # on profite des caractères de retour à la ligne '\n'

finished = False # pour savoir si la partie est finie
player = True # on initialise la valeur du joueur à vrai, elle nous sert à savoir qui joue
while(not finished): # tant que la partie n'est pas finie
    #choix automatique du joueur
    playerMark = ""
    if(player):
        playerMark = "X"
    else:
        playerMark = "O"

    # choix de l'emplacement
    print("Joueur ", playerMark, ", à toi de jouer !")
    validChoice = False
    while(not validChoice):
        choice = input("Case : ")
        if(grid.find(choice) == -1): # si case pas dispo (ou pas existante)
            print("Case indisponible !")
        else:
            validChoice = True

    # modification de la grille
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

    # lignes horizontales
    if((grid[0] == grid[3] == grid[6]) or (grid[8] == grid[11] == grid[14]) or (grid[16] == grid[19] == grid[22])):
        print("Joueur ", playerMark, " a gagné !")
        finished = True

    # lignes verticales
    if((grid[0] == grid[8] == grid[16]) or (grid[3] == grid[11] == grid[19]) or (grid[6] == grid[14] == grid[22])):
        print("Joueur ", playerMark, " a gagné !")
        finished = True

    # lignes diagonales
    if((grid[0] == grid[11] == grid[22]) or (grid[6] == grid[11] == grid[16])):
        print("Joueur ", playerMark, " a gagné !")
        finished = True

    # grille complète
    nCrosses = grid.count("X")
    nCircles = grid.count("O")
    if(nCrosses + nCircles == 9): # si il y a 9 cases remplies
        print("Egalité, fin de partie !")
        finished = True
    
    player = not player # on change de joueur