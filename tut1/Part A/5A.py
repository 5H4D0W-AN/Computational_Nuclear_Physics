import numpy as np
import matplotlib.pyplot as plt 


V0 = -25
a = 0.5
R = 5


def V(r):
	return V0/(1+np.exp((r-R)/a))

x = []
y = []

for i in np.arange(-10, 10, 0.01):
	x.append(i)
	y.append(V(i))

plt.plot(x, y)
plt.xlabel("r")
plt.grid(True)
plt.ylabel("V")
plt.show()
