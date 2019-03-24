import curses
import math

class PlotWindow:
    def __init__(self):
        self.screen = curses.initscr()
        curses.nocbreak()
        curses.noecho()
        self.screen.keypad(1)
        self.maxY, self. maxX = self.screen.getmaxyx()
        self.maxY -= 1
        self.maxX -= 1
        self.changeOfCoordsFunc = None
        self.updateChangeOfCoordsFunc()
        self.marker = "*"

    def updateChangeOfCoordsFunc(self):
        def f(p):
            return (self.maxY*(1-p[1]), self.maxX*p[0])
        self.changeOfCoordsFunc = f

    def addPoint(self, point):
        """
        Add point without updating the screen.
        Point is assumed to be in normalized coordinates.
        """
        p = self.changeOfCoordsFunc(point)
        self.screen.addstr(int(p[0]), int(p[1]), self.marker)

    def addPoints(self, points):
        """
        Add points without updating the screen.
        Points are assumed to be in normalized coordinates.
        """
        for point in points:
            self.addPoint(point)

    def updatePoints(self, points):
        """
        Clear screen and draw points.
        Points are assumed to be in normalized coordinates.
        """
        self.screen.clear()
        self.addPoints(points)
        self.screen.refresh()

    def updateWithPoint(self, point):
        """
        Add point and update.
        Preserves points that were previously on screen.
        Points are assumed to be in normalized coordinates.
        """
        self.addPoint(point)
        self.screen.refresh()

    def updateWithPoints(self, points):
        """
        Add points and update.
        Preserves points that were previously on screen.
        Points are assumed to be in normalized coordinates.
        """
        self.addPoints(points)
        self.screen.refresh()

    def printPoints(self, points):
        self.screen.clear()
        self.screen.move(0,0)
        for p in points:
            msg = "("+str(p[0])+","+str(p[1])+")\n"
            self.screen.addstr(msg)
        self.screen.refresh()

    def printConvertedPoints(self, points):
        self.screen.clear()
        self.screen.move(0,0)
        header = "Screen size: "
        header += ("width: "+str(self.maxX)+" ")
        header += ("height: "+str(self.maxY)+"\n")
        self.screen.addstr(header)
        for p in points:
            tp = self.changeOfCoordsFunc(p)
            msg = "("+str(tp[0])+","+str(tp[1])+")\n"
            self.screen.addstr(msg)
        self.screen.refresh()


    def clear(self):
        self.screen.clear()

    def waitForKeyPress(self):
        self.screen.getch()

    def close(self):
        curses.endwin()
