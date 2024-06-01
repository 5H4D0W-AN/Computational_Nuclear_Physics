import numpy as np
import matplotlib.pyplot as plt 
import math

def ff(n):
	if n==0 or n==1:
		return 1
	if n%2==1:
		return n*ff(n-2)
	if n%2==0:
		return (n-1)*ff(n-3)

def assoc_legendre(l, m, x):
	ans = 1.0
	if m>0:
		s = 1.0
		if(m%2 != 0):
			s = -1.0
		ans = s*ff(2*m-1)*pow((1.0-x*x), m/2)
	if l==m:
		return ans 
	ans1 = x*(2*m+1)*ans 
	if l==m+1:
		return ans1
	for i in range(m+2, l+1):
		t = (x*(2*i-1)*ans1 - (i+m-1)*ans)/(i-m)
		ans = ans1
		ans1 = t
	
	return ans1

def sp_har(theta, phi, l, m):
	a = (-1)**m*assoc_legendre(l, m, np.cos(theta))*np.exp(1j*m*phi)
	b = np.sqrt(((2*l+1)/(88/7))*(math.factorial(l-m)/math.factorial(l+m)))
	return a*b

phi = np.linspace(-np.pi, np.pi, 10000)
l = 2
m = 1

for theta in np.arange(0, np.pi, 0.628):
	plt.plot(phi, sp_har(theta, phi, l, m), label=f"theta={theta}")
plt.legend()
plt.title("Spherical Harmonics")
plt.xlabel("Phi")
plt.grid(True)
plt.show()
