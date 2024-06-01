import numpy as np
import matplotlib.pyplot as plt

def laguerre(n, x):
	if n==0:
		return np.ones(x.shape)
	if n==1:
		return 1-x
	else:
		a = np.ones(x.shape)
		b = 1-x
		for i in range(2, n+1):
			c = ((2*i-1-x)*b - (i-1)*a)/i
			a = b 
			b = c 
		return c 
x = np.arange(-1, 5, 0.01)
n = 6

for i in range(n):
	plt.plot(x, laguerre(i, x),label=f"{i}th order laguerre")
plt.legend()
plt.title("Laguerre Poly.")
plt.grid(True)
plt.show()