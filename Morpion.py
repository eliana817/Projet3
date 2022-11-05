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
screen.keypad(1)

rows, cols = screen.getmaxyx()

listeMenu = ["Jouer", "Quitter"]

def centrex(cols, texte) :
    return (cols - len(texte)) // 2

def centrey(rows) :
    return rows//2

def menuEtSelection(screen, indexSelection) :
    screen.clear()
    for index, element in enumerate(listeMenu) :
        y = rows//2 + index
        if index == indexSelection :
            screen.attron(curses.color_pair(2))
            screen.addstr(y, centrex(cols, element), element)
            #or screen.addstr(centrey(rows) + index, centrex(cols, element), element)
            screen.attroff(curses.color_pair(2))
        else :
            screen.addstr(y, centrex(cols, element), element)


def main(screen) :

    if (curses.has_colors() == True) :
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_MAGENTA)
        curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_RED)
        screen.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)



    indexSelection = 0
    menuEtSelection(screen, indexSelection)
    
    while True :
        key = screen.getch()

        if key == curses.KEY_DOWN and indexSelection == 0 :
            indexSelection = 1
        elif key == curses.KEY_UP and indexSelection == 1 :
            indexSelection = 0
        elif key == curses.KEY_ENTER or key in [10, 13] :
            if listeMenu[indexSelection] == "Jouer" :
                screen.clear()
                screen.addstr(2, centrex(cols, "Morpion"), "Morpion")
                screen.refresh()

                screen.getch()

            elif listeMenu[indexSelection] == "Quitter" :
                screen.clear()
                screen.addstr(centrey(rows), centrex(cols, "Vous allez quitter le jeu ..."), "Vous allez quitter le jeu ...")
                screen.refresh()
                time.sleep(2)
                
                screen.endwin()

        menuEtSelection(screen, indexSelection)
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


