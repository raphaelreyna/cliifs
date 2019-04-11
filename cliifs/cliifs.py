from cliifs import IFS
from cliifs import PlotWindow
from cliifs import SignalHandler
import argparse
import sys
import time

class cliifs:
    """
    Handles telling PlotWindow to display the IFS.
    """
    def __init__(self, filename):
        try:
            self.ifs = IFS.loadIFSFromFile(filename)
        except:
            print("You have passed an invalid file.")
            print("Please try again with a valid file.")
            sys.exit(-1)
        self.window = PlotWindow.PlotWindow()
        self.signalHandler = SignalHandler.SignalHandler()

    def show(self, stepsPerFrame, frameCount=1, delay=0):
        for i in range(frameCount):
            if self.signalHandler.terminate_now:
                return
            self.ifs.update(stepsPerFrame)
            #self.ifs.getNewPoints() is not working in this branch for some reason...
            # this is the work around.
            points = self.ifs.points
            self.ifs.points = []
            self.window.updateWithPoints(points)
            time.sleep(delay)
        self.window.waitForKeyPress()

    def close(self):
        self.window.close()

def main():
    """
    Handles arguments and running the program.
    """
    parser = argparse.ArgumentParser(description = "Render fractals in your terminal.")
    parser.add_argument("filename",
                        help="File that you want to render.")
    parser.add_argument("--iterations",
                        "-i",
                        help="Number of iterations to use. Default is 2000",
                        default=2000,
                        action="store",
                        nargs="?",
                        type=int)
    parser.add_argument("--color",
                        "-c",
                        help="Render using random colors.",
                        action="store_true")
    parser.add_argument("--animated",
                        "-a",
                        help="Animate the rendering process.",
                        action="store_true")
    parser.add_argument("--delay",
                        "-d",
                        help="Milliseconds by which to delay every frame.Only used if -a is also used. Default is 1.",
                        action="store",
                        default=1,
                        nargs="?",
                        type=float)
    parser.add_argument("--markers",
                        "-m",
                        help="String of characters to use at random as markers.",
                        default="*",
                        nargs="?",
                        type=str)
    args = parser.parse_args()
    filename = args.filename
    iterations = args.iterations
    markers = str(args.markers)
    c = cliifs(filename)
    c.window.markers = markers
    if args.color:
        c.window.useColor()
    if args.animated:
        delay = args.delay/1000
        c.show(1, iterations, delay)
    else:
        c.show(iterations)
    c.close()

if __name__ == "__main__":
    main()
