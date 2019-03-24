import curses
import random
import time
import math

def changeCoordsToCentered(y, x, maxX, maxY):
    return (2*x/maxX-1, 1-2*y/maxY)

def changeCoordsToCurses(x, y, maxX, maxY):
    return (0.5*maxY*(1-y), 0.5*maxX*(x+1))

def f1(x, y):
    return ((1/3)*(2*x-2), y)

def f2(x, y):
    return ((1/3)*(2*x-2)+(2/3),y)

if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    funcs = [f1, f2]
    point = (0,0)
    maxY, maxX = stdscr.getmaxyx()
    for i in range(1000):
        func = random.choice(funcs)
        point = func(*point)
        y, x = changeCoordsToCurses(point[0], point[1], maxX, maxY)
        stdscr.addstr(int(y), int(x), "*")
        stdscr.refresh()
        time.sleep(0.1)
    curses.endwin()

