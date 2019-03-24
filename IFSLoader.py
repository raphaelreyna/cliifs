import re

def makeFuncFromLine(line):
    parts = re.split('\ ', line)
    m = float(parts[0])
    b = float(parts[1])
    def f(x):
        return m*x+b
    return f

def loadFuncsFromFile(filename):
    f = open(filename, 'r')
    funcs = []
    if f.readline() == '2D\n':
        for line in f:
            func = makeFuncFromLine(line)
            funcs.append(func)
    return funcs
