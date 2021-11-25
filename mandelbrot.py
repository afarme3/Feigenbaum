#mandelbrot.py
#A class defining mandelbrot and hyperbrot objects, with rendering and plotting methods. 
import numpy as np
import matplotlib.pyplot as plt
import cmath

class mandelbrot:
    def __init__(self, resolution):
        self.resolution = resolution

    #Function to render mandelbrot set with pixel width/height "resolution"^2 and exponent "a"
    def render(self, a, precision=None, xRange=2, yRange=2, xCenter=0, yCenter=0):
        #Initialize precision default if no value is supplied
        if precision is None:
            precision = round(self.resolution/2)

        #Initialize constants for later plotting
        minX = xCenter-xRange
        maxX = xCenter+xRange
        minY = yCenter-yRange
        maxY = yCenter+yRange

        #Initialize output array. One row for real values, one row for complex values, one row for colormap. 
        output = [[],[],[],[]]

        #Iterate through pixels and run escape time algorithm
        for row in range(self.resolution):
            for coln in range(self.resolution):
                #Get coordinates for real and complex coordinates and add to output array
                x = minX + coln*(2*xRange)/self.resolution
                y = minY + row*(2*yRange)/self.resolution
                output[0].append(x)
                output[1].append(y)
                hasEscaped = False

                #Iterate the point to escape
                c = complex(x, y)
                z = 0
                for i in range(1, precision):
                    z = (z**a)+c
                    
                    #Check if the point has escaped and add the number of iterations needed to do so
                    if ((z.real**2)+(z.imag**2)) > 4:
                        output[2].append(1/i)
                        output[3].append((1-(1/i))**2)
                        hasEscaped = True
                        break
                    
                #If the point has escaped, set colormap index to 0
                if hasEscaped == False:
                    output[2].append(1)
                    output[3].append(1)

        
        self.points = output
    
    #Function to use matplot lib to plot the values
    def plot(self, colorMap="YlOrRd"):
        matplot = plt.figure()
        ax = matplot.add_subplot()

        #Create scatter plot
        ax.scatter(self.points[0], self.points[1], s=100/self.resolution, c=self.points[2], alpha=self.points[3], cmap=colorMap)
        plt.show()

class hyperbrot:
    def __init__(self, resolution):
        self.resolution = resolution

    #Function to render hyperbrot set with pixel width/height "resolution"^2 and exponent range 
    #Option renderBorder will save the points which escape to output array
    def render(self, renderInterior=True, renderBorder=False, precision=None, xRange=2, iRange=2, aRange=1, xCenter=0, iCenter=0, aCenter=2):
        #Initialize precision default if no value is supplied
        if precision is None:
            precision = round(self.resolution/2)

        #Initialize constants for later plotting
        minX = xCenter-xRange
        maxX = xCenter+xRange
        mini = iCenter-iRange
        maxi = iCenter+iRange
        minA = aCenter-aRange
        maxA = aCenter+aRange

        #Initialize output array. One row for real values, one row for complex values, one row for exponent, one row for colormap, one row for alphamap.
        output = [[],[],[],[],[]]

        #Iterate through exponents
        for exp in range(self.resolution):
            #Iterate through pixels and run escape time algorithm
            for row in range(self.resolution):
                for coln in range(self.resolution):
                    #Get coordinates for real and complex coordinates and add to output array
                    x = minX + coln*(2*xRange)/self.resolution
                    y = mini + row*(2*iRange)/self.resolution
                    a = minA + exp*(2*aRange)/self.resolution

                    hasEscaped = False

                    #Iterate the point to escape
                    c = complex(x, y)
                    z = 0
                    for i in range(1, precision):
                        z = (z**a)+c
                        
                        #Check if the point has escaped and add the number of iterations needed to do so if renderBorder is True
                        if ((z.real**2)+(z.imag**2)) > 4:
                            if renderBorder:
                                output[0].append(x)
                                output[1].append(y)
                                output[2].append(a)
                                output[3].append(1/i)
                                output[4].append(1-(1/i))
                            
                            hasEscaped = True
                            break
                        
                    #If the point has not escaped, set colormap index to 0
                    if hasEscaped == False:
                        if renderInterior:
                            output[0].append(x)
                            output[1].append(y)
                            output[2].append(a)
                            output[3].append((c.real**2)+(c.imag**2))
                            output[4].append(1)
            
            self.points = output
    
    #Function to use matplot lib to plot the values
    def plot(self, colorMap="YlOrRd", plotBorder=False, resolutionScale=100):
        matplot = plt.figure()
        ax = matplot.add_subplot(projection="3d")

        #Create scatter plot
        if plotBorder:
            ax.scatter(self.points[2], self.points[1], self.points[0], s=resolutionScale/self.resolution, c=self.points[3], alpha=self.points[4], cmap=colorMap)
        else:
            ax.scatter(self.points[2], self.points[1], self.points[0], s=resolutionScale/self.resolution, c=self.points[3], cmap=colorMap)

        ax.set_xlabel("Exponent (a)")
        ax.set_ylabel("Complex Axis (i)")
        ax.set_zlabel("Real Axis (x)")
        plt.show()


#test = hyperbrot(100)
#test.render(precision=40, xRange=2, iRange=2, aCenter=4, aRange=3)
#test.plot(resolutionScale=100, colorMap="cool")

test2 = mandelbrot(400)
test2.render(2.99, precision=100, xCenter=-0, xRange=1.5, yRange=1.5)
test2.plot(colorMap="magma")       

#Try vispy rendering








    

