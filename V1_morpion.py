
import random

titre = ["  __  __                  _          ", " |  \/  | ___  _ __ _ __ (_) ___  _ __", " | |\/| |/ _ \| '__| '_ \| |/ _ \| '_ \ "," | |  | | (_) | |  | |_) | | (_) | | | |", " |_|  |_|\___/|_|  | .__/|_|\___/|_| |_|", "                   |_|"] 

for partie in titre :
    print(partie)

print("")

morpion = [
"    0 1 2  ",
"   _______ ",
"0 | - - - |",
"1 | - - - |", 
"2 | - - - |",
"  |_______|"]

for k in range(len(morpion)) :
    print(morpion[k])

symboles = ["X", "O"]
nondispo = []
BOT = []
Joueur = []

print("")
syjoueur = str(input("Entrez si vous voulez être 'X' ou 'O' :\n"))

while syjoueur != "X" and syjoueur != "O" :
    syjoueur = str(input("Entrez 'X' ou 'O' :\n"))
    print("")

if syjoueur == "X" :
    syBOT = "O"
else : 
    syBOT = "X"

def coordjoueur(nondispo, Joueur) :

    case = str(input("Entrez les coordonnées de la case où vous souhaitez vous placer (colonne d'abord 0 à 2(inclus), puis ligne allant de 0 à 2(inclus)) :\n"))
    print("")

    while len(case) != 3 or (case[0] != "0" and case[0] != "1" and  case[0] != "2") or (case[2] != "0" and case[2] != "1" and case[2] != "2") :
        case = str(input("Entrez bien des coordonnées valides avec un espace entre chaques valeurs :\n"))
        print("")

    x = int(case[0])
    y = int(case[2])
    
    choix = (x, y)

    while choix in nondispo :
        case = str(input("Veuillez entrer des coordonnées valides et non déjà prises :\n"))
        print("")
        x = int(case[0])
        y= int(case[1])

    nondispo.append(choix)

    Joueur.append(choix)

    return x, y, nondispo, Joueur

def coordBOT(nondispo, BOT) :

    x = random.randint(0, 2)
    y = random.randint(0, 2)

    choixBOT = (x,y)

    while choixBOT in nondispo :
        x = random.randint(0,2)
        y = random.randint(0,2)
        choixBOT = (x,y)

    nondispo.append(choixBOT)
    BOT.append(choixBOT)

    return x, y, nondispo, BOT

def affichage(morpion, syjoueur, x, y) :
    x = 2 * x + 4
    y = y + 2
    ordonnee = list(morpion[y])
    ordonnee[x] = syjoueur
    ordonnee = "".join(ordonnee)
    morpion[y] = ordonnee

    for k in range(len(morpion)) :
        print(morpion[k])

    return morpion

def avantageJ(OccJoueurCol, OccJoueurLine, OccJoueurDiag1, OccJoueurDiag2) :

    totalCol =0
    totalLine = 0

    for k in range (2) :
        ColCount = OccJoueurCol.count(k)
        if totalCol < ColCount :
            totalCol = ColCount

    for i in range (2) :
        LineCount = OccJoueurLine.count(i)
        if totalLine < LineCount :
            totalLine = LineCount

    TotalCount = []

    TotalCount.extend([totalCol, totalLine, OccJoueurDiag1, OccJoueurDiag2])
    
    avantageJoueur = max(TotalCount)

    return avantageJoueur


def avantageB(OccBOTCol, OccBOTLine, OccBOTDiag1, OccBOTDiag2) :

    totalCol =0
    totalLine = 0

    for k in range (2) :
        ColCount = OccBOTCol.count(k)
        if totalCol < ColCount :
            totalCol = ColCount

    for i in range (2) :
        LineCount = OccBOTLine.count(i)
        if totalLine < LineCount :
            totalLine = LineCount

    TotalCount = []

    TotalCount.extend([totalCol, totalLine, OccBOTDiag1, OccBOTDiag2])
    
    avantageBOT = max(TotalCount)

    return avantageBOT


def tourJoueur(OccJoueurCol, OccJoueurLine, OccJoueurDiag1, OccJoueurDiag2, avantageJoueur, tour, nondispo, Joueur, syjoueur, morpion) :
    print("")
    print("C'est à vous !")
    print("")
    x, y, nondispo, Joueur = coordjoueur(nondispo, Joueur)
    morpion = affichage(morpion, syjoueur, x, y)
    tour += 1
    for k in range (len(Joueur)) :
        OccJoueurCol.append(Joueur[k][0])
        OccJoueurLine.append(Joueur[k][1])
        if Joueur[k][0] == Joueur[k][1] :
            OccJoueurDiag1 += 1
            if Joueur[k] == (1,1) :
                OccJoueurDiag2 += 1
        elif Joueur[k] == (0,2) or Joueur[k] == (2,0) :
            OccJoueurDiag2 += 1
    
    avantageJoueur = avantageJ(OccJoueurCol, OccJoueurLine, OccJoueurDiag1, OccJoueurDiag2) 

    return avantageJoueur, tour, Joueur, nondispo, morpion



def tourBOT(OccBOTCol, OccBOTLine, OccBOTDiag1, OccBOTDiag2, avantageBOT, tour, BOT, nondispo, syBOT, morpion) :
    print("")
    print("C'est au tour du BOT : ")
    print("")
    x, y, nondispo, BOT = coordBOT(nondispo, BOT)
    morpion = affichage(morpion, syBOT, x, y)
    tour += 1
    for i in range (len(BOT)) :
        OccBOTCol.append(BOT[i][0])
        OccBOTLine.append(BOT[i][1])
        if BOT[i][0] == BOT[i][1] :
            OccBOTDiag1 += 1
            if BOT[i] == (1,1) :
                OccBOTDiag2 += 1
        elif BOT[i] == (0,2) or BOT[i] == (2,0) :
            OccBOTDiag2 += 1

    avantageBOT = avantageB(OccBOTCol, OccBOTLine, OccBOTDiag1, OccBOTDiag2) 

    return avantageBOT, tour, BOT, nondispo, morpion


avantageJoueur = 0
avantageBOT = 0

tour = 0

commence = random.randint(0, 1)

while avantageJoueur < 3 and avantageBOT < 3 and tour < 9:
    
    OccJoueurCol = []
    OccBOTCol = []
    OccJoueurLine = []
    OccBOTLine = []
    OccJoueurDiag1 = 0
    OccJoueurDiag2 = 0
    OccBOTDiag1 = 0
    OccBOTDiag2 = 0

    if commence == 0 :
        avantageJoueur, tour, Joueur, nondispo, morpion = tourJoueur(OccJoueurCol, OccJoueurLine, OccJoueurDiag1, OccJoueurDiag2, avantageJoueur, tour, Joueur, nondispo, syjoueur, morpion)
     
        avantageBOT, tour, BOT, nondispo, morpion = tourBOT(OccBOTCol, OccBOTLine, OccBOTDiag1, OccBOTDiag2, avantageBOT, tour, BOT, nondispo, syBOT, morpion)

    else :
        avantageBOT, tour, BOT, nondispo, morpion = tourBOT(OccBOTCol, OccBOTLine, OccBOTDiag1, OccBOTDiag2, avantageBOT, tour, BOT, nondispo, syBOT, morpion)
        
        avantageJoueur, tour, Joueur, nondispo, morpion = tourJoueur(OccJoueurCol, OccJoueurLine, OccJoueurDiag1, OccJoueurDiag2, avantageJoueur, tour, Joueur, nondispo, syjoueur, morpion)
        
    

if tour == 9 :
    print("")
    print("Egalité !")
elif avantageBOT > avantageJoueur :
    print("")
    print("Vous avez perdu !")
elif avantageJoueur > avantageBOT :
    print("")
    print("Vous avez gagné !")





