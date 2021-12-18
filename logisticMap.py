#logisticMap.py - a program to render high-resolution images of the feigenbaum bifurcation cascade (logistic map)

#Imports
import numpy as np
import matplotlib.pyplot as plt
import mpl_scatter_density


#Initialize starting values and output arrays
rvals = []
xvals = []
lvals = []
lyapunovVals = [[],[]]

#Run logistic map equation to generate r vs x plot
r = 1
nXiters = 200
rScaler = 0.0004
x = 0.7
while r <= 4:
    tempLvals = []
    for xIter in range(0,nXiters):
        x = r*x*(1-x)
        l = np.log(abs(r - 2*r*x))
        rvals.append(r)
        xvals.append(x)
        lvals.append(l)
        tempLvals.append(l)
    lyapunovVals[0].append(r)
    lyapunovVals[1].append(np.mean(tempLvals))
    r += rScaler    


#plot the map
colorscale = np.divide(np.array(rvals), 4)
figure = plt.figure(tight_layout=True)
plot1 = figure.add_subplot(1,1,1, projection="scatter_density")
#plot1.scatter_density(rvals, xvals, dpi=50, downres_factor=1, cmap="Blues")
#plot1.scatter(lyapunovVals[0], lyapunovVals[1], s=0.1, c=lyapunovVals[1], cmap="winter")
plot1.scatter(rvals, xvals, s=0.05, c=lvals, cmap="viridis")
#plt.axhline(y=0, color='r', linestyle='-')
plt.xlabel("R (resolution of "+str(rScaler)+")")
plt.ylabel("X (Iterated "+str(nXiters)+" times per R value)")
plt.title("Logistic Map (3.5 < r)")
#plt.savefig("logisticMap.png", orientation="landscape", bbox_inches="tight", dpi=200)
plt.show()
    