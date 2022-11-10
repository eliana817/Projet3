from random import randint

list = ["Pierre", "Feuille", "Ciseaux", "Rock"]

player_name=input('Quel est ton nom ? ')
print("")
computer_name=("BOT Chifoumi")

player = True

def unJoueur(player) : 
    score_BOT = 0
    score_Player = 0
    while player == True:
        computer = list[randint(0,2)]
        player = input('Pierre, Feuille ou Ciseaux ? ')
        print("")

        if player == computer:
            print("BOT Chifoumi a joué {}".format(computer))
            print("")
            print("Egalité ! Le BOT Chifoumi a pensé comme toi !")
            print("")
        elif player == "Rock" : 
            print("Tu as gagné !", player_name, "a écrasé totalement", computer_name)
            print("")
            score_Player += 1
        elif player == "Pierre" or player == "pierre":
            if computer == "Feuille":
                print("BOT Chifoumi a joué {}".format(computer))
                print("")
                print("Tu as perdu !", computer_name, "a contré", player_name)
                print("Think about use a Rock not a Pierre")
                print("")   
                score_BOT += 1
            else:
                print("BOT Chifoumi a joué {}".format(computer))
                print("")
                print("Tu as gagné !", player_name, "a écrasé", computer_name)
                print("")
                score_Player += 1
        elif player == "Feuille" or player == "feuille" :
            if computer == "Ciseaux":
                print("BOT Chifoumi a joué {}".format(computer))
                print("")
                print("Tu as perdu...", computer_name, "a découpé", player_name)
                print("")
                score_BOT += 1
            else:
                print("BOT Chifoumi a joué {}".format(computer))
                print("")
                print("Tu as gagné !", player_name, "a contré", computer_name)
                print("")
                score_Player += 1
        elif player == "Ciseaux" or player == "ciseaux":
            if computer == "Pierre":
                print("BOT Chifoumi a joué {}".format(computer))
                print("")
                print("Tu as perdu...", computer_name, "a écrasé", player_name)
                print("")
                score_BOT += 1
            else:
                print("BOT Chifoumi a joué {}".format(computer))
                print("")
                print("Tu as gagné !", player_name, "a découpé", computer_name)
                print("")
                score_Player += 1
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
            print("Score = {}({}) à {}({})".format(score_Player,player_name, score_BOT, "BOT Chifoumi"))
            return

    if score_Player > score_BOT :
        print("Score = {}({}) à {}({}). Vous avez gagné !".format(score_Player, player_name, score_BOT,  "BOT Chifoumi"))
    elif score_Player < score_BOT :
        print("Score = {}({}) à {}({}). Vous avez perdu !".format(score_Player, player_name, score_BOT, "BOT Chifoumi"))
    else :
        print("Egalité ! Score = {}({}) à {}({}).".format(score_Player, player_name, score_BOT, "BOT Chifoumi")) 

unJoueur(player)
    
    



    
    



