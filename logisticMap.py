#logisticMap.py - a program to render high-resolution images of the logistic map bifurcation diagram

#Imports
import numpy as np
import matplotlib.pyplot as plt
import mpl_scatter_density


#Initialize starting values and output arrays
x0 = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
rvals = []
xvals = []
lyapunovVals = [[],[]]

#Run logistic map equation to generate r vs x plot
#for xinit in x0:
rInit = 3.56995
r = rInit
nXiters = 200
rScaler = 0.00001
x = 0.7
while r <= 4:

    lvals = []
    for xIter in range(0,nXiters):
        x = r*x*(1-x)
        rvals.append(r)
        xvals.append(x)
        lvals.append(np.log(abs(r - 2*r*x)))
    lyapunovVals[0].append(r)
    lyapunovVals[1].append(np.mean(lvals))
    r += rScaler    


#plot the map
colorscale = np.divide(np.array(rvals), 4)
figure = plt.figure(tight_layout=True)
plot1 = figure.add_subplot(1,1,1, projection="scatter_density")
#plot1.scatter_density(rvals, xvals, dpi=50, downres_factor=1, cmap="Blues")
#plot1.scatter(lyapunovVals[0], lyapunovVals[1], s=0.1, c=lyapunovVals[1], cmap="winter")
plot1.scatter(rvals, xvals, s=0.1, c=colorscale, cmap="viridis")
plt.axhline(y=0, color='r', linestyle='-')
plt.xlabel("R (resolution of "+str(rScaler)+")")
plt.ylabel("X (Iterated "+str(nXiters)+" times per R value)")
plt.title("Logistic Map ("+str(rInit)+" < r)")
#plt.savefig("logisticMap.png", orientation="landscape", bbox_inches="tight", dpi=200)
plt.show()
    