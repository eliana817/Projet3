from random import randint

list = ["Pierre", "Feuille", "Ciseaux"]

player_name=input('Quel est ton nom ? ')
print("")
computer_name=("BOT Chifoumi")

#computer = list[randint(0,2)]

player = True

def unJoueur(player) :
    scoreBOT = 0
    scorePlayer = 0
    while player == True:
        computer = list[randint(0,2)]
        player = input('Pierre, Feuille ou Ciseaux ? ')
        print("")
        if player == computer:
            print("Egalité !")
            print("")
        elif player == "Pierre" or player == "pierre":
            if computer == "Feuille":
                print("Tu as perdu !", computer_name, "a contré", player_name)
                print("")
                scoreBOT += 1
            else:
                print("Tu as gagné !", player_name, "a écrasé", computer_name)
                print("")
                scorePlayer += 1
        elif player == "Feuille" or player == "feuille" :
            if computer == "Ciseaux":
                print("Tu as perdu...", computer_name, "a découpé", player_name)
                print("")
                scoreBOT += 1
            else:
                print("Tu as gagné !", player_name, "a contré", computer_name)
                print("")
                scorePlayer += 1
        elif player == "Ciseaux" or player == "ciseaux":
            if computer == "Pierre":
                print("Tu as perdu...", computer_name, "a écrasé", player_name)
                print("")
                scoreBOT += 1
            else:
                print("Tu as gagné !", player_name, "a découpé", computer_name)
                print("")
                scorePlayer += 1
        else:
            print("Attention tu as mal fais ton choix, alors veilles à bien écrire ce que tu souhaites jouer.")
            print("")           
        
        player = input("Voulez-vous rejouer ? Entrez Oui ou Non :")
        print("")
        if player == "Oui" or player == "Non" or player == "non" or player == "oui" :
            if player == "Oui" or player == "oui" : 
                player = True
            else:
                player = False
        else :
            player = False
            print("Vous avez quitté le jeu car vous n'avez pas répondu correctement")
            print("")
            print("Score = {}({}) à {}({})".format(scorePlayer,player_name, scoreBOT, "BOT Chifoumi"))
            return

    if scorePlayer > scoreBOT :
        print("Score = {}({}) à {}({}). Vous avez gagné !".format(scorePlayer, player_name, scoreBOT,  "BOT Chifoumi"))
    elif scorePlayer < scoreBOT :
        print("Score = {}({}) à {}({}). Vous avez perdu !".format(scorePlayer, player_name, scoreBOT, "BOT Chifoumi"))
    else :
        print("Egalité ! Score = {}({}) à {}({}).".format(scorePlayer, player_name, scoreBOT, "BOT Chifoumi")) 

unJoueur(player)
    
    #player = True
    #computer = list[randint(0,2)]



