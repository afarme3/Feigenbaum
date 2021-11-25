#logistic3d.py: a program to get plot the logistic map in 3-d with point density on the z-axis. 

#Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as spatial
import mpl_scatter_density


#Initialize starting values and output arrays
x0 = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
rvals = []
xvals = []
outputVals = []

#Run logistic map equation to generate r vs x plot
#for xinit in x0:
r = 3
nXiters = 200
rScaler = 0.0005
x = x0[6]
while r <= 4:  
        for xIter in range(0,nXiters):
            x = r*x*(1-x)
            rvals.append(r)
            xvals.append(x)
            outputVals.append([r, x])
        r += rScaler 

#Gets an array which stores [r,x] values
combined = np.array(outputVals)
#Uses scipy.spatial tree to get the number of neighbors in the radius of each point
tree = spatial.KDTree(combined)
radius = rScaler*5
neighbors = tree.query_ball_tree(tree, radius)

#Convert number of neighbors to point density
density = []
for neighbor in neighbors:
    neighborDensity = len(neighbor)/(radius**2)
    density.append((neighborDensity/len(rvals)))


colorscale = np.divide(np.array(rvals), 4)

#Plot in 3d
matplot = plt.figure()
ax = matplot.add_subplot(projection="3d")
ax.scatter(rvals, xvals, density, s=0.01, c=colorscale, cmap="autumn")
ax.set_xlabel("R (resolution of "+str(rScaler)+")")
ax.set_ylabel("X ("+str(nXiters)+" iterations)")
ax.set_zlabel("Point Density (radius "+str(radius)+")")
plt.show()

quit()

#Plot 2d R vs density - looks like lyapunov exponent!
matplot = plt.figure()
ax = matplot.add_subplot()
ax.scatter(rvals, density, s=0.01, c=colorscale, cmap="autumn")
ax.set_xlabel("R (resolution of "+str(rScaler)+")")
ax.set_ylabel("Point Density (radius "+str(radius)+")")
plt.show()