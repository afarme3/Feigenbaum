#logisticMap.py - a program to render high-resolution images of the feigenbaum bifurcation cascade (logistic map)

#Imports
import numpy as np
import matplotlib.pyplot as plt
import mpl_scatter_density


#Initialize starting values and output arrays
x0 = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
rvals = []
xvals = []

#Run logistic map equation to generate r vs x plot
#for xinit in x0:
r = 3.56
nXiters = 200
rScaler = 0.00005
x = x0[6]
while r <= 4:  
        for xIter in range(0,nXiters):
            x = r*x*(1-x)
            rvals.append(r)
            xvals.append(x)
        r += rScaler    


#plot the map
colorscale = np.divide(np.array(rvals), 4)
figure = plt.figure(tight_layout=True)
plot1 = figure.add_subplot(1,1,1, projection="scatter_density")
#plot1.scatter_density(rvals, xvals, dpi=50, downres_factor=1, cmap="Blues")
plot1.scatter(rvals, xvals, s=0.01, c=colorscale, cmap="winter")
plt.xlabel("R (resolution of "+str(rScaler)+")")
plt.ylabel("X (Iterated "+str(nXiters)+" times per R value)")
plt.title("Logistic Map (3.5 < r)")
#plt.savefig("logisticMap.png", orientation="landscape", bbox_inches="tight", dpi=200)
plt.show()
    