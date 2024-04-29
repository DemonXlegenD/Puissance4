import random as rand

#Grille de base
grille1 = [
[" "," ", " ", " "," ", " ", " "],
[" "," ", " ", " "," ", " ", " "],
[" "," ", " ", " "," ", " ", " "],
[" "," ", " ", " "," ", " ", " "],
[" "," ", " ", " "," ", " ", " "],
[" "," ", " ", " "," ", " ", " "]
]

#Exercice 1

nbr_jt_rouge = 21
nbr_jt_jaune = 21
ligne_grille = 6 #inutiles avec les fonctions que j'ai utilisées
colonne_grille = 7 #inutiles avec les fonctions que j'ai utilisées
jeton_rouge = "*"
jeton_jaune = "o"


#Exercice 2 

def vide_grille():
    structure =  [[" "," ", " ", " "," ", " ", " "],
[" "," ", " ", " "," ", " ", " "],
[" "," ", " ", " "," ", " ", " "],
[" "," ", " ", " "," ", " ", " "],
[" "," ", " ", " "," ", " ", " "],
[" "," ", " ", " "," ", " ", " "]]
    return structure


##Exercice 3 

def affiche_grille(grille):
    print("     0 1 2 3 4 5 6")
    print("    ---------------")
    for i in range(0,len(grille)):
        print(f"{i}   |", end="")
        for j in range(len(grille)+1):            
            print(grille[i][j], end="|")
        print(f"  {i} ")
        print("    ---------------")
    print("     0 1 2 3 4 5 6")
    print("")


##Exercice 4 

def colonne_remplie(colonne,grille):
    colonne_est_remplie = False
    #créer un tableau qui contient que des false si la colonne est remplie
    colonne_jouable = [False]*(7)
    for i in range(0,len(grille)):
        if(grille[i][colonne]!=" "):
            colonne_jouable[i] = False
        else:
            colonne_jouable[i] = True

    #toutes les cases de la colonnes sont remplies
    if(colonne_jouable == [False]*7):
        colonne_est_remplie = True
    else:
        colonne_est_remplie = False

    return colonne_est_remplie

##Exercice 5 

def lache_jeton(jeton, colonne, grille):

    #la colonne est remplie
    if(colonne_remplie(colonne,grille)):
        print( "La colonnes choisie est pleine")

    #la colonne n'est pas remplie
    else:
        place_libre = True
        #on part du bas de la colonne puis on remonte
        for i in range(len(grille)-1, -1,-1):  
            #si la case est vide est qu'aucun jeton n'a été laché auparavant
            if(grille[i][colonne] ==' ' and place_libre):
                grille[i][colonne] = jeton
                place_libre= False

##Exercice 6

#fonction qui gère l'égalité
def is_egalite(structure):
    structure_pleine = True
    for i in range(0, len(structure)):
        for j in range(0, len(structure)+1):
            if(structure[i][j]==" "):
                structure_pleine = False
    return structure_pleine

#fonction qui gère si il y a un gagnant avec 4 pions à la verticale
def verif_verticale(structure, joueur):
    verif = False
    for i in range(len(structure)-1,2,-1):
        for j in range(0, len(structure)+1):
            if(structure[i][j]==joueur):
                if(structure[i][j]==structure[i-1][j] and structure[i][j]==structure[i-2][j] and structure[i][j]==structure[i-3][j]):
                    verif = True
    return verif

#fonction qui gère si il y a un gagnant avec 4 pions à l'horizontale
def verif_horizontale(structure, joueur):
    verif = False

    for i in range(0, len(structure)):

        #on part de la gauche de la grille
        for j in range( 0, len(structure)-2):
            if(structure[i][j]==joueur):
                if(structure[i][j]==structure[i][j+1] and structure[i][j]==structure[i][j+2] and structure[i][j]==structure[i][j+3]):

                    verif = True     
    return verif

#fonction qui gère si il y a un gagnant avec 4 pions à la diagonale croissante
def verif_diagonalecroissante(structure, joueur):
    verif = False

    #on part du bas de la grille
    for i in range(len(structure)-1,2,-1):

        #on part de la gauche de la grille
        for j in range(0,len(structure)-2):

            if(structure[i][j]==joueur):
                if(structure[i][j]==structure[i-1][j+1] and structure[i][j]==structure[i-2][j+2] and structure[i][j]==structure[i-3][j+3]):
                    verif = True
    return verif

#fonction qui gère si il y a un gagnant avec 4 pions à la diagonale décroissante
def verif_diagonaledecroissante(structure, joueur):
    verif = False

    #on part du bas de la grille
    for i in range(len(structure)-1,2,-1):

        #on part de la gauche de la grille à partir de la colonne 3
        for j in range(3,len(structure)+1):

            if(structure[i][j]==joueur):
                if(structure[i][j]==structure[i-1][j-1] and structure[i][j]==structure[i-2][j-2] and structure[i][j]==structure[i-3][j-3]):
                    verif = True
    return verif

#fonction qui gère la victoire d'un joueur
def is_victoire(structure, joueur):
    if(verif_verticale(structure, joueur)):
        return True
    elif(verif_horizontale(structure, joueur)):
        return True
    elif(verif_diagonalecroissante(structure, joueur)):
        return True
    elif(verif_diagonaledecroissante(structure, joueur)):
        return True
    else:
        return False


##Exercice 7

def propose_colonne(structure):

    nbraleatoire = rand.randint(0,6)
    while colonne_remplie(nbraleatoire, structure):
       nbraleatoire = rand.randint(0,6)
    
    print(f"Vous pouvez choisir la colonne {nbraleatoire} par exemple.\n")

##Exercice 8 (pas fini)

# def propose_colonne_2(joueur, structure):
#     structure2 = structure

#     conseil = 0
#     bon = True
#     while bon:
#         nbraleatoire = rand.randint(0,6)
#         while colonne_remplie(nbraleatoire, structure):
#            nbraleatoire = rand.randint(0,6)
#         lache_jeton(joueur, nbraleatoire, structure2)
#         if(is_victoire(structure2, joueur)):
#             print(f"Vous pouvez choisir la colonne {nbraleatoire}, vous aurez plus de chance de gagner.\n")
#             bon = False
#         else:
#             bon = True



##FONCTIONS ANNEXES

#affiche les colonnes restantes sous forme de string
def affiche_colonne(structure):
    colonnes = ""
    for i in range(0,len(structure)+1):
        if not(colonne_remplie(i,structure)):
            colonnes = colonnes + str(i) + ("," if i!=6 else "")
        else:
            colonnes = colonnes + ""

    return colonnes

#regarde si la partie continue ou non
def partie_continue(structure , joueur):
    if(is_victoire(structure, joueur)):
        print("Le joueur ", "1" if joueur=="*" else "2", " a gagné la partie!\n")
        return False
    elif(is_egalite(structure)):
        print("Match nul!\n")
        return False
    else:
        return True


running = False
lancer = True

"""DEBUT DU PROGRAMME"""

#demande au joueur si il veut lancer la partie
while lancer:
    print("Bonjour et Bienvenue à puissance 4! Le jeu pour s'amuser en famille ou entre amis!\n")

    try:
        question1 = input("Voulez-vous lancer une partie? [Y/N] : ").upper()

        if(question1=="Y" or question1=="YES"):
            running = True
            lancer = False
            grille1 = vide_grille()
        elif(question1=="N" or question1 == "NO"):
            running = False
            lancer = False
            print("Dommage... ça aurait été amusant. Revenez si vous en sentez l'envie!\n")
        else:
            print("Choisissez soit Y ou soit N.\n")
    except:
        print("Veuillez choisir soit Y ou soit N.\n")

#lance la partie
while running:

    print("Et c'est parti!\n")
    jouer = True
    joueur1_is_playing = True
    joueur2_is_playing = False
    
    while jouer:


        while joueur1_is_playing:
            print("TOUR JOUEUR 1:\n")

            affiche_grille(grille1)
            print("")
            propose_colonne(grille1)
            # propose_colonne_2(jeton_rouge, grille1)
            try:
                number1 = int(input(f"Lachez votre pion dans une colonne ({affiche_colonne(grille1)}) : "))

                if(number1>=0 and number1<=6):
                    if(colonne_remplie(number1,grille1)):
                        print("La colonne est déjà remplie, choisissez en une autre!\n")
                    else:
                        lache_jeton(jeton_rouge, number1, grille1)
                        nbr_jt_rouge -= 1
                        print(f"Il vous reste encore {nbr_jt_rouge} jetons rouges.\n")
                        joueur1_is_playing = False
                        joueur2_is_playing = True
                else:
                    print("Choisissez un nombre valide entre ceux présentés.\n")
            except:
                print("Veuillez selectionner un nombre valide.\n")

        print("Grille après tour joueur 1 : \n")
        affiche_grille(grille1)

        #si le jeu continue
        if jouer:

            jouer = partie_continue(grille1 ,jeton_rouge)

            #si un joueur a gagné
            if not(jouer):
                joueur1_is_playing = False
                joueur2_is_playing = False

        while joueur2_is_playing:
            print("TOUR JOUEUR 2:\n")

            affiche_grille(grille1)
            print("")
            propose_colonne(grille1)
            # propose_colonne_2(jeton_jaune, grille1)
            try:
                number2 = int(input(f"Lachez votre pion dans une colonne ({affiche_colonne(grille1)}) : "))

                if(number2>=0 and number2<=6):
                    if(colonne_remplie(number2,grille1)):
                        print("La colonne est déjà remplie, choisissez en une autre!\n")
                    else:
                        lache_jeton(jeton_jaune, number2, grille1)
                        nbr_jt_jaune -= 1
                        print(f"Il vous reste encore {nbr_jt_jaune} jetons jaunes.\n")
                        joueur1_is_playing = True
                        joueur2_is_playing = False
                else:
                    print("Choisissez un nombre valide entre ceux présentés.\n")
            except:
                print("Veuillez selectionner un nombre valide.\n")

        print("Grille après tour joueur 2 : \n")
        affiche_grille(grille1)
        if jouer:
            jouer = partie_continue(grille1 ,jeton_jaune)

            if not(jouer):
                joueur1_is_playing = False
                joueur2_is_playing = False

    relancer = True

    #demande au joueur si il veut relancer
    while relancer:
        grille1 = vide_grille()
        print("Maintenant que la partie est terminée!\n")
        try:
            question2 = input("Voulez-vous en relancer une? [Y/N] : " ).upper()
            if(question2=="Y" or question2=="YES"):
                running = True
                relancer = False
            elif(question2=="N" or question2 == "NO"):
                running = False
                relancer = False
                print("Dommage... ça aurait été amusant. Revenez si vous en sentez l'envie!\n")
            else:
                print("Choisissez soit Y ou soit N.\n")
        except:
            print("Veuillez choisir soit Y ou soit N.\n")