import numpy as np
import matplotlib.pyplot as plt
import math

a = 80
nmax = 3


for n in range(0, nmax+1):
    for n_p in range(0, n+1, 1):
        n_z = n - n_p
        del_osc = []
        energy = []
        for i in np.arange(-1, 1, 0.01):
            f = np.power((1 - (4/3)*i)*(1 + (2/3)*i)**2, -1/6)
            h_omega = 41*pow(a, -1/3)*f
            del_osc.append(i)
            e = h_omega * (n + 1.5 - (1/3)*i*((2*n_z)-n_p))
            energy.append(e)

        plt.plot(del_osc, energy, label = f"n={n}, np={n_p}, nz={n_z}")


plt.ylabel("Energy")
plt.xlabel("Deformation Parameter")
plt.title("Anisotropic Harmonic Oscillator")
plt.grid(True)
# plt.legend()        
plt.show()