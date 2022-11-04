import curses
from curses import wrapper
import sys

print("Initialisation du jeu... ")

def main(main_screen) :
   raise Exception

screen = curses.initscr()
curses.curs_set(0)

#if curses.has_colors():
    #curses.start_color()


if (curses.has_colors() == True) :
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_MAGENTA)
    screen.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)



screen.addstr(1, 38, "Morpion")


screen.addstr(22, 20, "Appuyez sur n'importe quel touche  pour quitter")

screen.refresh()

screen.getch()


curses.endwin()
 

print("Vous avez fermez le jeu.")

wrapper(main)

