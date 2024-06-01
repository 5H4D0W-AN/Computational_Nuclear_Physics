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

def differentiate(n, x):
	if n==0:
		return Ysi(0, x)*(x**2-1)
	elif n==1:
		return -1*(8**0.5)*x*Ysi(0, x) + (x*x-1)*Ysi(1, x)
	else:
		return 2*np.sqrt(n*(n-1))*Ysi(n-2, x) - np.sqrt(8*n)*x*Ysi(n-1, x) + (x*x-1)*Ysi(n, x)

def integrate(n, x0, xn, f):
	h = (xn-x0)/n
	ans = 0
	for i in range(0, n+1):
		if(i==0) or (i==n):
			ans += f(x0 + i*h)
		elif i%2 != 0:
			ans += 4*f(x0+i*h)
		else :
			ans += 2*f(x0+i*h)
	ans = (ans*h/3)
	return ans

K = np.zeros([5, 5])
for i in range(0, 5):
	for j in range(0, 5):
		c = integrate(100, -10, 10, lambda x: differentiate(j, x)*Ysi(i, x))
		K[i][j] = round(-c/2, 4)

P = np.zeros([5, 5])
for i in range(0, 5):
	for j in range(0, 5):
		c  = integrate(100, -10, 10, lambda x: Ysi(j, x)*Ysi(i, x)*x*x)
		P[i][j] = round(c/2, 4)
print(K+P)