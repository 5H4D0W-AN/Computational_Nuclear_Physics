import numpy as np
import matplotlib.pyplot as plt 

def legendre(n, x):
	if n==0:
		return 1
	elif n==1:
		return x
	else:
		return ((2*n-1)*x*legendre(n-1, x)-(n-1)*legendre(n-2, x))/n

x = np.arange(-1, 1, 0.01)
for i in range(0, 6):
	y = [legendre(i, xx) for xx in x]
	plt.plot(x, y, label=f"{i}th order legendre poly.")
plt.xlabel("x")
plt.ylabel("Leg. Poly. function")
plt.grid(True)
plt.legend()
plt.show()