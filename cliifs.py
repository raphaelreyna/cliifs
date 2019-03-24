import curses
import random
import time
import math
import IFSLoader
import sys

def changeCoordsToCurses(x, y, maxX, maxY):
    return (maxY*(1-y), maxX*x)

if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    filename = sys.argv[1]
    funcs = IFSLoader.loadFuncsFromFile(filename)
    point = 0
    maxY, maxX = stdscr.getmaxyx()
    for i in range(6000):
        func = random.choice(funcs)
        point = func(point)
        y, x = changeCoordsToCurses(point, 0.5, maxX-1, maxY-1)
        stdscr.addstr(int(y), int(x), "*")
        stdscr.refresh()
    stdscr.getch()
    curses.endwin()

