import random
import time

liste = ["Pierre", "Feuille", "Ciseaux"]

nom = str(input("Entrez votre nom :\n"))
print("")

valeurJoueur = str(input("Entrez Pierre, Feuille ou Ciseaux :\n"))
print("")

while valeurJoueur != "Pierre" and ValeurJoueur != "Feuille" and valeurJoueur != "Ciseaux" :
    valeurJoueur = str(input("Soyez certain de bien entrer une de ces valeurs : Pierre, Feuille ou Ciseaux"))
    print("")

print("{} joue contre ...".format(valeurJoueur))
print("")

time.sleep(2)
valeurOrdi = random.choice(liste)
print(ValeurOrdi)
