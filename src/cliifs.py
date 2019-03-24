import IFS
import PlotWindow
import argparse

class cliifs:
    def __init__(self, filename):
        self.ifs = IFS.loadIFSFromFile(filename)
        self.window = None

    def generatePoints(self, numberOfIterations):
        self.ifs.update(numberOfIterations)

    def showPoints(self):
        self.window = PlotWindow.PlotWindow()
        self.window.updatePoints(self.ifs.points)
        self.window.waitForKeyPress()

    def close(self):
        self.window.close()

if __name__ == "__main__":
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
    args = parser.parse_args()
    filename = args.filename
    iterations = args.iterations
    c = cliifs(filename)
    c.generatePoints(iterations)
    c.showPoints()
    c.close()

