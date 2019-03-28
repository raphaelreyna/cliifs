from src import IFS
from src import PlotWindow
import argparse
import sys

class cliifs:
    def __init__(self, filename):
        try:
            self.ifs = IFS.loadIFSFromFile(filename)
        except:
            print("You have passed an invalid file.")
            print("Please try again with a valid file.")
            sys.exit(-1)
        self.window = PlotWindow.PlotWindow()

    def generatePoints(self, numberOfIterations):
        self.ifs.update(numberOfIterations)

    def showPoints(self):
        self.window.updatePoints(self.ifs.points)
        self.window.waitForKeyPress()

    def close(self):
        self.window.close()

def main():
    parser = argparse.ArgumentParser(description = "Render fractals in your terminal.")
    parser.add_argument("filename",
                        help="File that you want to render.")
    parser.add_argument("--iterations",
                        "-i",
                        help="Number of iterations to use.",
                        default=1000,
                        action="store",
                        nargs="?",
                        type=int)
    parser.add_argument("--color",
                        "-c",
                        action="store_true")
    args = parser.parse_args()
    filename = args.filename
    iterations = args.iterations
    c = cliifs(filename)
    if args.color:
        c.window.color = True
    c.generatePoints(iterations)
    c.showPoints()
    c.close()

if __name__ == "__main__":
    main()
