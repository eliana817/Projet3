import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

 
X_symbol = ["__  __", "\ \/ /", " \  / ", " /  \ ", "/_/\_\ "]
Y_symbol = ["  ___ ", " / _ \ ", "| | | |", "| |_| |", " \___/ "]

def display_symbol(sy, X_symbol, Y_symbol) :
    symbole = ""
    if sy == "X" :
        for part in X_symbol :
            symbole += part + "\n"
        return symbole
    elif sy == "O" :
        for part in Y_symbol :
            symbole += part + "\n"
        return symbole

sign = 0
 

global board
board = [[" " for x in range(3)] for y in range(3)]
 

def winner(b, l) :
    #Vérifie si une des conditions gagnantes est bien remplie
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))
 

def get_text(i, j, gb, l1, l2) :
    """Ajoute le symbole du joueur dans la case sélectionné 
    Vérifie à chaque tour si il y a un gagnant ou une égalité : affiche un message correspondant à la situation si c'est le cas
    """
    global sign
    if board[i][j] == ' ' :
        if sign % 2 == 0 :
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else :
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=display_symbol(board[i][j], X_symbol, Y_symbol))
    if winner(board, "X") :
        box = messagebox.showinfo("Victoire !", "Joueur 1 a gagné le match.")
        gb.destroy()
    elif winner(board, "O") :
        box = messagebox.showinfo("Victoire !", "Joueur 2 a gagné le match")
        gb.destroy()
    elif(isfull()) :
        box = messagebox.showinfo("Egalité !", "C'est une égalité.")
        gb.destroy()
        
        
 

def isfree(i, j) :
    return board[i][j] == " "
 

def isfull() :
    flag = True
    for i in board:
        if(i.count(' ') > 0):
            flag = False
    return flag
 

def gameboard_pl(game_board, l1, l2) :
    #construit la grille pour le morpion constituée de boutons
    global button
    button = []
    for i in range(3) :
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3) :
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
 

def pc() :
    #Défini où le BOT va jouer
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else :
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner)-1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge)-1)
            return edge[move]


def get_text_pc(i, j, gb, l1, l2):
    """Ajoute le symbole du BOT dans la case sélectionné 
    Vérifie à chaque tour si il y a un gagnant ou une égalité : affiche un message correspondant à la situation si c'est le cas
    """
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=display_symbol(board[i][j], X_symbol, Y_symbol))
    x = True
    if winner(board, "X"):
        x = False
        box = messagebox.showinfo("Victoire !", "Tu as gagné le match.")
        gb.destroy()
    elif winner(board, "O"):
        x = False
        box = messagebox.showinfo("Victoire !", "BOT TicTacToe gagne le match.")
        gb.destroy()
    elif(isfull()):
        x = False
        box = messagebox.showinfo("Egalité !", "C'est une égalité.")
        gb.destroy()
    if(x):
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)
 

def gameboard_pc(game_board, l1, l2):
    #construit la grille pour le morpion constituée de boutons
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=8, width=16)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
 

def withpc(game_board): 
    """On crée une nouvelle fenêtre avec 2 boutons qui indiques qui joue
    Prend en argument la fenêtre actuelle pour ensuite la détruire et créer la nouvelle
    """
    game_board.destroy()
    game_board = Tk()
    game_board.title("Morpion")
    l1 = Button(game_board, text = "Joueur 1 : X", width= 20)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text = "BOT TicTacToe : O",
                width = 20, state = DISABLED)
     
    l2.grid(row = 2, column = 1)
    gameboard_pc(game_board, l1, l2)
 

def withplayer(game_board): 
    """On crée une nouvelle fenêtre avec deux boutons qui indiques qui joue
    Prend en argument la fenêtre actuelle pour ensuite la détruire et créer la nouvelle
    """
    game_board.destroy()
    game_board = Tk()
    game_board.title("Morpion")
    l1 = Button(game_board, text = "Joueur n°1 : X",  width = 10)
     
    l1.grid(row = 1, column = 1)
    l2 = Button(game_board, text = "Joueur n°2 : O",
                width = 10, state = DISABLED)
     
    l2.grid(row = 2, column = 1)
    gameboard_pl(game_board, l1, l2)

def play():
    #Fonction qui crée la fenêtre du menu principal avec les différents boutons
    menu = Tk()
    menu.geometry("500x500")
    menu.title("Morpion de Jspa")
    wpc = partial(withpc, menu)
    wpl = partial(withplayer, menu)
     
    head = Button(menu, text = "Morpion de Jspa | Veuillez choisir votre mode de jeu ",
                  activeforeground = 'cyan',
                  activebackground = "cyan", bg = "cyan",
                  fg = "black", width = 500, font = 'helvetica', bd = 5)
     
    B1 = Button(menu, text = "Jouer contre un Ordinateur", command = wpc,
                activeforeground = 'cyan',
                activebackground = "pink", bg = "cyan",
                fg = "black", width = 500, font = 'helvetica', bd = 5)
     
    B2 = Button(menu, text = "Jouer à deux joueurs", command = wpl, activeforeground = 'cyan',
                activebackground = "pink", bg = "cyan", fg = "black",
                width = 500, font = 'helvetica', bd = 5)
     
    B3 = Button(menu, text = "Quitter le jeu...", command = menu.quit, activeforeground = 'cyan',
                activebackground = "pink", bg = "cyan", fg = "black",
                width = 500, font = 'helvetica', bd = 5)

    head.pack(side = 'top')
    B1.pack(side = 'top')
    B2.pack(side = 'top')
    B3.pack(side = 'top')
    menu.mainloop()
 

if __name__ == '__main__':
    play()
