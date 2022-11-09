import curses
from curses import wrapper
import sys
import time


print("Initialisation du jeu... ")

#def main_s(screen_main) :
   #raise Exception

screen = curses.initscr()
curses.curs_set(0)
curses.mousemask(-1)
curses.cbreak()
curses.noecho()
screen.keypad(1)

rows, cols = screen.getmaxyx()

listeMenu = ["Jouer", "Quitter"]
MenuJouer = ["Rejouer", "Retour"]

def centrex(cols, texte) :
    return (cols - len(texte)) // 2

def centrey(rows) :
    return rows//2


def menuEtSelection(screen, Selection) :
    screen.clear()
    for index, element in enumerate(listeMenu) :
        y = rows//2 + index
        if index == Selection :
            screen.attron(curses.color_pair(2))
            screen.addstr(y, centrex(cols, element), element)
            #or screen.addstr(centrey(rows) + index, centrex(cols, element), element)
            screen.attroff(curses.color_pair(2))
        else :
            screen.addstr(y, centrex(cols, element), element)

def menuJouer(winHome, Select) :
    winHome.clear()
    for index, element in enumerate(MenuJouer) :
        if index == Select :
            winHome.attron(curses.color_pair(2))
            winHome.addstr(centrey(rows)+index, 5, element)
            winHome.attroff(curses.color_pair(2))
        else :
            winHome.addstr(centrey(rows) + index, 5, element)

def affichage(screen) :

    case1 = curses.newwin(7, 14, centrey(rows) - 9, 61)
    case1.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    case1.refresh()
    screen.refresh()

    case2 = curses.newwin(7, 14, centrey(rows) - 9, 61 + 16)
    case2.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    case2.refresh()
    screen.refresh()

    case3 = curses.newwin(7, 14, centrey(rows) - 9, 61 + 32)
    case3.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    case3.refresh()
    screen.refresh()
   
    case4 = curses.newwin(7, 14, centrey(rows) - 1, 61)
    case4.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    case4.refresh()
    screen.refresh()

    case5 = curses.newwin(7, 14, centrey(rows) - 1, 61 + 16)
    case5.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    case5.refresh()
    screen.refresh()

    case6 = curses.newwin(7, 14, centrey(rows) - 1, 61 + 32)
    case6.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    case6.refresh()
    screen.refresh()

    case7 = curses.newwin(7, 14, centrey(rows) + 7, 61)
    case7.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    case7.refresh()
    screen.refresh()
   
    case8 = curses.newwin(7, 14, centrey(rows) + 7, 61 + 16)
    case8.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    case8.refresh()
    screen.refresh()
  
    case9 = curses.newwin(7, 14, centrey(rows) + 7, 61 + 32)
    case9.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    case9.refresh()
    screen.refresh()

def main(screen) :
    
    morpion = ["__  __                  _          ", "|  \/  | ___  _ __ _ __ (_) ___  _ __", " | |\/| |/ _ \| '__| '_ \| |/ _ \| '_ \ "," | |  | | (_) | |  | |_) | | (_) | | | |", "  |_|  |_|\___/|_|  | .__/|_|\___/|_| |_|", " |_|"]                
    

    if (curses.has_colors() == True) :
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_MAGENTA)
        curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_RED)
        screen.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)



    Selection = 0 #index pour le menu principal
    menuEtSelection(screen, Selection)
    
    
    while True :
        
        menuEtSelection(screen, Selection)

        key = screen.getch()

        if (key == curses.KEY_DOWN  and Selection == 0) or (key == ord('s') and Selection == 0) :
            Selection = 1
        elif (key == curses.KEY_UP and Selection == 1) or (key == ord('z') and Selection == 1) :
            Selection = 0
        elif key == curses.KEY_ENTER or key in [10, 13] :
            if listeMenu[Selection] == "Jouer" :
                screen.clear()
                for i, ligne in enumerate(morpion) :
                    screen.addstr(i, centrex(cols, ligne), ligne)

                
                winHome = curses.newwin(20, 30, centrey(rows) - 10, 5)
                winHome.keypad(1)
                winHome.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)                
                winHome.refresh()
                screen.refresh()  

                winJeu = curses.newwin (25, 50, centrey(rows) - 10, 59)
                winJeu.keypad(1)
                winJeu.bkgd(' ', curses.color_pair(2) | curses.A_BOLD)
                winJeu.refresh()
                screen.refresh()

                grille = affichage(screen)


                Select = 0 #index pour le menu une fois dans le jeu

                while True :

                    menuJouer(winHome, Select)

                    cle = winHome.getch()

                    if (cle == curses.KEY_DOWN and Select == 0) or (cle == ord('s') and Select == 0) :
                        Select = 1
                    elif (cle == curses.KEY_UP and Select == 1) or (cle == ord('z') and Select == 1) :
                        Select = 0
                    elif cle == curses.KEY_ENTER or key in [10, 13] :
                        if MenuJouer[Select] == "Retour" :
                            #putChar(win, ' ')
                            #win = None
                            break

                    
                        
                                          
                

            elif listeMenu[Selection] == "Quitter" :
                screen.clear()
                screen.addstr(centrey(rows), centrex(cols, "Vous allez quitter le jeu ..."), "Vous allez quitter le jeu ...")
                screen.refresh()
                time.sleep(2)
                
                screen.endwin()

        #menuEtSelection(screen, Selection)
        screen.refresh()


    
    
    """
    screen.addstr(rows - 2, centrex(cols, "Appuyez sur sur 'q' pour quitter"), "Appuyez sur 'q' pour quitter")
    
    while True :
        key = screen.getch()
        if key == ord('q') :
            curses.endwin()

    screen.refresh()
    """



curses.wrapper(main)
 

print("Vous avez fermez le jeu.")


