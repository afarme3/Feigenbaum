# gauss.py - a script to render gauss iterative map bifurcation diagrams
import matplotlib.pyplot as plt
import math
import numpy as np

class gauss:
    def __init__(self, bresolution, a):
        self.bRes = bresolution
        self.alpha = a

    def render(self, nIterations=100, InitialCondition=0):
        self.nIters = nIterations
        b = -1
        x = InitialCondition
        output = [[],[]]
        while b <= 1:
            for i in range(0,self.nIters):
                x = math.exp((-self.alpha*(x**2))) + b
                output[0].append(x)
                output[1].append(b)
                b += self.bRes
        self.points = output

    def plot(self, colormap="autumn", pointSize=0.1):

        #Initialize matplotlib plot
        matplot = plt.figure()
        ax = matplot.add_subplot()

        #Plot values
        ax.scatter(self.points[1], self.points[0], s=pointSize, c=self.points[1], cmap=colormap)
        ax.set_xlabel("Beta (Resolution of "+str(self.bRes)+")")
        ax.set_ylabel("X (Iterated "+str(self.nIters)+" times per beta")
        plt.title("Gauss Iterated Map with alpha="+str(self.alpha))

        plt.show()

class multiGauss:
    def __init__(self, aresolution, bresolution, aMin=3, aMax=7):
        self.aRes = aresolution
        self.bRes = bresolution
        self.aMin = aMin
        self.aMax = aMax

    def render(self, nIterations=100, InitialCondition=0):
        self.nIters = nIterations
        a = self.aMin
        output = [[],[],[]]

        while a < self.aMax:
            b = -1
            x = InitialCondition

            while b <= 1:
                for i in range(0,self.nIters):
                    x = math.exp((-a*(x**2))) + b
                    output[0].append(x)
                    output[1].append(b)
                    output[2].append(a)
                    b += self.bRes
            a += self.aRes
        self.points = output

    def plot(self, colormap="autumn", pointSize=0.1):

        #Initialize matplotlib plot
        matplot = plt.figure()
        ax = matplot.add_subplot(projection="3d")

        #Plot values
        ax.scatter(self.points[1], self.points[2], self.points[0], s=pointSize, c=self.points[1], cmap=colormap)
        ax.set_xlabel("Beta (Resolution of "+str(self.bRes)+")")
        ax.set_ylabel("X (Iterated "+str(self.nIters)+" times per beta")
        ax.set_zlabel("Alpha (Resolution of "+str(self.aRes)+")")
        plt.title("3d Gauss Map")

        plt.show()
