# tentMap.py - a program to compute and render the tent map bifurcation diagram

#Imports
import numpy as np
import matplotlib.pyplot as plt
import mpl_scatter_density

# Initialize starting values and output arrays
mu = 1
nXiters = 150
muScaler = 0.0002
muVals = []
xVals = []

#Iterate the tent map
while mu <= 2:
        x = 0.5  
        for xIter in range(0,nXiters):
            x = mu*min(x, 1-x)
            muVals.append(mu)
            xVals.append(x)
        mu += muScaler    
    
#plot the map
colorscale = np.divide(np.array(muVals), 2)
figure = plt.figure(figsize=(11, 8.5), tight_layout=True)
plot1 = figure.add_subplot(1,1,1, projection="scatter_density")
#plot1.scatter_density(rvals, xvals, dpi=50, downres_factor=1, cmap="Blues")
plot1.scatter(muVals, xVals, s=0.001, c=colorscale, cmap="viridis")
plt.xlabel("Mu (resolution of "+str(muScaler)+")")
plt.ylabel("X (Iterated "+str(nXiters)+" times per Mu value)")
plt.title("Tent Map (Full)")
plt.savefig("tentMap.png", orientation="landscape", bbox_inches="tight", dpi=200)
#plt.show()