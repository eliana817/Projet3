import curses
from curses import wrapper
import sys

print("Initialisation du jeu... ")

#def main(main_screen) :
   # raise Exception


screen = curses.initscr()

curses.curs_set(0)
screen.addstr(1, 38, "Morpion")











screen.addstr(22, 20, "Appuyez sur n'importe quel touche  pour quitter")

screen.refresh()


c = screen.getch()


curses.endwin()
 

print("Vous avez fermez le jeu.")

#wrapper(main)

