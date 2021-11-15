#mandelbrot.py
#A class defining mandelbrot and hyperbrot objects, with rendering and plotting methods. 
import numpy as np
import matplotlib.pyplot as plt
import cmath

class mandelbrot:
    def __init__(self, name):
        self.name = name

    #Function to render mandelbrot set with pixel width "resolution" and exponent "a"
    def render(self, a, precision, resolution):
        #Initialize center points. X is the real axis and Y is the complex axis.
        x = 0
        y = 0

        #Initialize constants for later plotting
        xRange = 6
        yRange = 4
        height = round(resolution/yRange)
        minX = x-xRange/2
        maxX = x+xRange/2
        minY = y-yRange/2
        maxY = y+yRange/2

        #Initialize output array. One row for real values, one row for complex values, one row for colormap. 
        output = [[],[],[]]

        #Iterate through pixels and run escape time algorithm
        for row in range(height):
            for coln in range(resolution):
                #Get coordinates for real and complex coordinates and add to output array
                x = minX + coln * xRange/resolution
                y = minY + row * yRange/resolution
                output[0].append(x)
                output[1].append(y)
                hasEscaped = False

                #Iterate the point to escape
                for i in range(1,precision+1):
                    z = complex(x, y)
                    z = z**a
                    x = z.real  
                    y = z.imag

                    #Check if the point has escaped and add the number of iterations needed to do so
                    if x*x + y*y > 4:
                        output[2].append(i)
                        hasEscaped = True
                        break
                #If the point has escaped, set colormap index to 0
                if hasEscaped == False:
                    output[2].append(0)

        
        self.points = output
    
    #Function to use matplot lib to plot the values
    def plot(self):
        matplot = plt.figure()
        ax = matplot.add_subplot()

        #Create scatter plot
        ax.scatter(self.points[0], self.points[1], s=0.01, c=self.points[2], cmap="winter")
        plt.show()

test = mandelbrot("test")
test.render(2, 500, 500)
test.plot()
        








    

