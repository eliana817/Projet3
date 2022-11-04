import curses
import sys

print("Initialisation du jeu... ")

screen = curses.initscr()

screen.refresh()

curses.napms(5000)
curses.endwin()

print("Vous avez fermez le jeu.")


