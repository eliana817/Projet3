from random import randint

list = ["Pierre", "Feuille", "Ciseaux"]

player_name=input('Quel est ton nom ? ')
computer_name=("BOT Chifoumi")

computer = list[randint(0,2)]

player = True

while player == True:
    player = input('Pierre, Feuille ou Ciseaux ? ')
    if player == computer:
        print("Egalité !")
    elif player == "Pierre":
        if computer == "Feuille":
            print("Tu as perdu !", computer_name, "a contré", player_name)
        else:
            print("Tu as gagné !", player_name, "a écrasé", computer_name)
    elif player == "Feuille":
        if computer == "Ciseaux":
            print("You lose!", computer_name, "a découpé", player_name)
        else:
            print("You win!", player_name, "a contré", computer_name)
    elif player == "Ciseaux":
        if computer == "Pierre":
            print("Tu as perdu...", computer_name, "a écrasé", player_name)
        else:
            print("Tu as gagné !", player_name, "a découpé", computer_name)
    else:
        print("Attention tu as mal fais ton choix, alors veilles à bien écrire ce que tu souhaites jouer.")
    player = True
    computer = list[randint(0,2)]
