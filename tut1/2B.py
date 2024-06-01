import numpy as np
import matplotlib.pyplot as plt 
import math

def hermite(n, x):
	if n == 0:
		return np.ones_like(x)
	if n == 1:
		return 2*x
	return 2*x*hermite(n-1, x)-2*n*hermite(n-2, x)

def Ysi(n, x):
	return (np.exp(-(x*x)/2))/(np.sqrt(math.factorial(n)*(2**n))*pow(22/7, 0.25))*hermite(n, x)

n = 3
x = np.linspace(-8, 8, 10000)
for i in range(0, n+1):
	y = Ysi(i, x)
	plt.plot(x, y, label=f"{i}th order wave")
plt.xlabel("x")
plt.grid(True)
plt.ylabel("Harmonic Oscillator wave function")
plt.legend()
plt.show()