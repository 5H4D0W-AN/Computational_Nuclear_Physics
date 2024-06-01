import numpy as np
import matplotlib.pyplot as plt
import math

nmax= 3

def E(np, nz, rho):
    e= np+nz + 1.5
    e= e- 0.333*rho*(nz+nz-np)
    return e

x= np.linspace(-1, 1, 1000)

for n in range(0, nmax+1, 1):
    for np in range(0, n+1):
        nz= n-np
        plt.plot(x, E(np, nz, x), label=f"n={n}, np= {np}, nz= {nz}")
        

plt.ylabel("Energy")
plt.xlabel("Rho")
# plt.xlim(-1.2, 2.5)
plt.title("Anisotropic HO")
plt.grid(True)
plt.legend()        
plt.show()