import numpy as np
import matplotlib.pyplot as plt
import math

c = -0.1
d = -0.0225

for n in range (0, 4, 1):
    for l in range(n, -1, -2):
        l_square = l*(l+1)
        ls1 = l/2         #for j = l+1/2
        ls2 = -(l+1)/2    #for j = l-1/2
        e1 = (n+1.5) + c*ls1 + d*l_square
        e2 = (n+1.5) + c*ls2 + d*l_square
        e3 = (n+1.5)
        
        x = (0, 1, 2, 3, 4, 5, 6, 8)
        y1 = []
        y2 = []
        for i in x:
            if i<3 or l==0:
                y1.append(e3)
                y2.append(e3)
            else: 
                y1.append(e1)
                y2.append(e2)
        
        if l==0:
            plt.plot(x, y1, label = f"N= {n}, l = {l}, j= {l+0.5}")
        else:
            plt.plot(x, y1, label = f"N= {n}, l = {l}, j= {l+0.5}")
            plt.plot(x, y2, label = f"N= {n}, l = {l}, j= {l-0.5}")

plt.ylim(1,5)
plt.ylabel("Energy")
plt.title("Independent Particle Model")
plt.grid(True)
plt.legend()        
plt.show()