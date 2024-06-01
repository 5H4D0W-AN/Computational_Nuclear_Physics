import numpy as np
import math
import matplotlib.pyplot as plt 

def assoc_lag(x, n, k):
	if n==0:
		return np.ones_like(x)
	elif n==1:
		return -x-k+1
	return ((k+n)*assoc_lag(x, n-1, k))/n - (assoc_lag(x, n-1, k+1)*x)/n

def dblfact(n):
    if n==0 or n==1:
        return 1
    if n%2==1:
        return n*dblfact(n-2)
    if n%2==0:
        return (n-1)*dblfact(n-3)

def assoc_legendre(l, m, x):
	ans = 1.0
	if m>0:
		s = 1.0
		if(m%2 != 0):
			s = -1.0
		ans = s*dblfact(2*m-1)*pow((1.0-x*x), m/2)
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

def sp(n, l, m, r):
	a = 0.529e-10
	b = np.sqrt(((2/(n*a*math.factorial(n+l))))**3*math.factorial(n-l-1)/(2*n))
	c = np.exp(-r/(n*a)) * ((2*r)/(n*a))**l 
	d = assoc_lag((2*r)/(n*a), n-l-1, 2*l+1)
	return b*c*d 

def ang(theta, phi, l, m):
	a = (-1)**m*assoc_legendre(l, m, np.cos(theta))*np.exp(1j*m*phi)
	b = np.sqrt(((2*l+1)/(88/7))*(math.factorial(l-m)/math.factorial(l+m)))
	return a*b

a = 0.529 * (10**-10)

N = [1, 2, 2, 2, 3, 3, 3, 4]
L = [0, 0, 1, 1, 0, 1, 2, 0]
M = [0, 0, 1, 0, 0, 0, 0, 0]

theta1 = np.pi / 4
phi1 = np.pi / 4
r = np.linspace(-a, 14 * a, 10000)

# Define radial_part and angular_part functions (not provided in the snippet)

fig, axs = plt.subplots(2, 4, figsize=(12, 6))

for i, ax in enumerate(axs.flatten()):
    radial_par = sp(N[i], L[i], M[i], r)
    ax.plot(r / a, radial_par, label=f"n={N[i]}, l={L[i]}, m={M[i]}")
    ax.set_xlabel("r/a")
    ax.set_ylabel("Radial term of wave function")
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(2, 4, figsize=(12, 6))

for i, ax in enumerate(axs.flatten()):
    radial_par = sp(N[i], L[i], M[i], r)
    print("for nlm= ", N[i], L[i], M[i], ", Theta and Phi= ", theta1, ", ", phi1)
    print("   the angular part= ", ang(np.pi/4, np.pi/4,L[i], M[i]))
    total_wavef = abs(sp(N[i], L[i], M[i], r) * ang(np.pi/4, np.pi/4,L[i], M[i]))**2
    ax.plot(r / a, total_wavef, label=f"n={N[i]}, l={L[i]}, m={M[i]}")
    ax.set_xlabel("r/a")
    ax.set_ylabel("Total wave function")
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.show()