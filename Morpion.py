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

def menuJouer(win, Select) :
    win.clear()
    for index, element in enumerate(MenuJouer) :
        if index == Select :
            win.attron(curses.color_pair(2))
            win.addstr(centrey(rows)+index, 5, element)
            win.attroff(curses.color_pair(2))
        else :
            win.addstr(centrey(rows) + index, 5, element)
            

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


        key = screen.getch()

        if key == curses.KEY_DOWN and Selection == 0 :
            Selection = 1
        elif key == curses.KEY_UP and Selection == 1 :
            Selection = 0
        elif key == curses.KEY_ENTER or key in [10, 13] :
            if listeMenu[Selection] == "Jouer" :
                screen.clear()
                for i, ligne in enumerate(morpion) :
                    screen.addstr(i, centrex(cols, ligne), ligne)

                
                win = curses.newwin(20, 30, centrey(rows) - 10, 5)
                win.keypad(1)
                win.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)                
                win.refresh()
                screen.refresh()   

                Select = 0 #index pour le menu une fois dans le jeu

                while True :

                    menuJouer(win, Select)

                    cle = win.getch()

                    if cle == curses.KEY_DOWN and Select == 0 :
                        Select = 1
                    elif cle == curses.KEY_UP and Select == 1 :
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

        menuEtSelection(screen, Selection)
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


