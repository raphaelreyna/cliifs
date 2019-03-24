import re
from random import choice

def make1DFuncFromLine(line):
    parts = re.split('\ ', line)
    m = float(parts[0])
    b = float(parts[1])
    def f(p):
        return (m*p[0]+b, 0.5)
    return f

def loadFuncsFromFile(filename):
    f = open(filename, 'r')
    funcs = []
    if f.readline() == '1D\n':
        for line in f:
            func = make1DFuncFromLine(line)
            funcs.append(func)
    f.close()
    return funcs

def loadIFSFromFile(filename):
    funcs = loadFuncsFromFile(filename)
    ifs = IFS()
    ifs.funcs = funcs
    return ifs

class IFS:
    def __init__(self):
        self.funcs = []
        self.point = (0,0)
        self.points = []
        self.oldWidth = 1
        self.oldHeight = 1
        self.vMax = 1
        self.vMin = 0
        self.oldvMin = 0
        self.hMax = 1
        self.hMin = 0
        self.oldhMin = 0

    def update(self, numberOfTimes):
        shouldUpdateHeight = False
        shouldUpdateWidth = False
        oldWidth = 0
        oldHeight = 0
        generatedPoints = []
        for i in range(numberOfTimes):
            func = choice(self.funcs)
            self.point = func(self.point)
            generatedPoints.append(self.point)
            if self.point[0] > self.hMax:
                oldHeight = self.hMax - self.hMin
                self.hMax = self.point[0]
                self.shouldUpdateWidth = True
            if self.point[0] < self.hMin:
                oldHeight = self.hMax - self.hMin
                self.oldhMin = self.hMin
                self.hMin = self.point[0]
                self.shouldUpdateWidth = True
            if self.point[1] > self.vMax:
                oldWidth = self.vMax - self.vMin
                self.vMax = self.point[1]
                self.shouldUpdateHeight = True
            if self.point[1] < self.vMin:
                oldWidth = self.vMax - self.vMin
                self.oldvMin = self.vMin
                self.vMin = self.point[1]
                self.shouldUpdateHeight = True

        if shouldUpdateWidth | shouldUpdateHeight:
            if shouldUpdateWidth:
                self.oldWidth = oldWidth
            if shouldUpdateHeight:
                self.oldHeight = oldHeight
            self.renormalize()

        normalizedPoints = self.normalizePoints(generatedPoints)
        self.points += normalizedPoints

    def renormalize(self):
        height = self.vMax - self.vMin
        width = self.hMax - self.hMin
        result = map(lambda p: (
            ((self.oldWidth*p[0]+self.oldhMin)-self.hMin)/width,
            ((self.oldHeight*p[1]+self.oldvMin)-self.vMin)/height),
            self.points)
        self.points = list(result)

    def normalizePoint(self, point):
        height = self.vMax - self.vMin
        width = self.hMax - self.hMin
        return ((x-self.hMin)/width, (y-self.vMin)/height)

    def normalizePoints(self, points):
        height = self.vMax - self.vMin
        width = self.hMax - self.hMin
        result = map(lambda p: (
            (p[0]-self.hMin)/width,
            (p[1]-self.vMin)/height),
                     points)
        return list(result)
