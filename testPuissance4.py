line1 = [1, 2, 3, 4, 5]
line2 = [6, 7, 8, 9, 10]
line3 = [11, 12, 13, 14, 15]
line4 = [16, 17, 18, 19, 20]
line5 = [21, 22, 23, 24, 25]
lines = [line1, line2, line3, line4, line5]

# affichage de la grille de départ
for line in lines:
    textLine = ""
    for character in line:
        textLine += str(character) + "\t"
    print(textLine)

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
        choice = int(input("Case : "))
        for line in lines:
            if(line.__contains__(choice)): # si case pas dispo (ou pas existante)
                validChoice = True
        if(not validChoice):
            print("Case indisponible !")

    # modification de la grille
    if(1 <= choice <= 5):
        line1[choice - 1] = playerMark
    elif(6 <= choice <= 10):
        line2[choice - 6] = playerMark
    elif(11 <= choice <= 15):
        line3[choice - 11] = playerMark
    elif(16 <= choice <= 20):
        line4[choice - 16] = playerMark
    elif(21 <= choice <= 25):
        line5[choice - 21] = playerMark

    # affichage de la grille modifiée
    for line in lines:
        textLine = ""
        for character in line:
            textLine += str(character) + "\t"
        print(textLine)

    # lignes horizontales
    

    # lignes verticales
    

    # lignes diagonales
    

    # grille complète
    nCharacters = 0
    for line in lines:
        for character in line:
            if(character == "X" or character == "O"):
                nCharacters += 1
    if(nCharacters == 25): # si il y a 25 cases remplies
        print("Egalité, fin de partie !")
        finished = True
    
    player = not player # on change de joueur