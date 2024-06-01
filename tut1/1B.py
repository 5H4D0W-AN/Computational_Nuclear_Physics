import numpy as np
import matplotlib.pyplot as plt 

def hermite(n, x):
	if n==0:
		return np.ones_like(x)
	if n==1:
		return 2*x
	return 2*x*hermite(n-1, x) - 2*n*hermite(n-2, x)


print("For x = 1.8, value of 3rd hemite Polynomial is:", hermite(3, 1.8))
n = 6
x = np.linspace(-1, 1, 10000)

for i in range(0, n):
	H = hermite(i, x)
	plt.plot(x, H, label=f"{i}th order")
plt.xlabel("x")
plt.grid(True)
plt.ylabel("Hermite Polynomial")
plt.legend()
plt.show()