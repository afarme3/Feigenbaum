#logisticIterator.py: A script to print values of the 

#Imports
import numpy as np
import matplotlib.pyplot as plt
import mpl_scatter_density


#Initialize starting values and output arrays
xvals = [0.4, 0.9, 0.4, 0.4, 0.4, 0.4]
rvals = [2.6, 2.6, 0.9, 3.1, 3.49, 3.6]

#Run logistic map equation to generate r vs x plot
for index in range(0,6):  
    x=xvals[index]
    r=rvals[index]
    results=[]
    for xIter in range(0,10):
        x = r*x*(1-x)
        results.append(format(x, ".3f"))
    print(results)
exit()

#plot the map
colorscale = np.divide(np.array(rvals), 4)
figure = plt.figure()
plot1 = figure.add_subplot(1,1,1, projection="scatter_density")
plot1.scatter_density(rvals, xvals, dpi=50, downres_factor=1, color="red")
plt.show()
    