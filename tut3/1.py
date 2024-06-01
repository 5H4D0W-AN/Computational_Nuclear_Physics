import matplotlib.pyplot as plt
import math
import numpy as np

dE = 0.001
m = 938.272
hc = 197.3269631
L = 20
pi = math.pi
psi0 = 0
dpsi0 = 0.01
Emin = -25
Emax = ((5.5*pi*hc/L)**2)/(2*m)-25

n = 100
h = L/n
x0 = -L/2    
toll = 1e-4
tol = [0.3e-2,0.4e-3,0.3e-3,0.5e-3,1e-4]
nos=0
E = Emin

def V(x):
    if (x<-10) or (x>10):
        return 0
    else:
        return -25

def f1(x,psi,dpsi):
    return dpsi

def f2(x,psi,dpsi):
    return -2*m*(E-V(x))*psi/(hc**2)

def rk4_simul(f1,f2,t0,x0,y0,h):
    k1 = h*f1(t0, x0, y0)
    l1 = h*f2(t0, x0, y0)

    k2 = h*f1(t0+h/2, x0+k1/2, y0+l1/2)
    l2 = h*f2(t0+h/2, x0+k1/2, y0+l1/2)

    k3 = h*f1(t0+h/2, x0+k2/2, y0+l2/2)
    l3 = h*f2(t0+h/2, x0+k2/2, y0+l2/2)

    k4 = h*f1(t0+h, x0+k3, y0+l3)
    l4 = h*f2(t0+h, x0+k3, y0+l3)

    x1 = x0 + (k1+2*k2+2*k3+k4)/6
    y1 = y0 + (l1+2*l2+2*l3+l4)/6
    
    return x1, y1

while (E<Emax):
    psi2 = psi0
    dpsi2 = dpsi0
    x2 = x0
    x_list = []
    psi_list = []
    for i in range(n):
        psi1 = psi2
        dpsi1 = dpsi2
        x1 = x2
        x_list.append(x1)
        psi_list.append(psi1)
        psi2, dpsi2 = rk4_simul(f1,f2,x1,psi1,dpsi1,h)
        x2 = x1 + h
    if (abs(psi2)<toll):
        x_list.append(x2)
        psi_list.append(psi2)
        plt.plot(x_list,psi_list, label = str(25+E))
        E=E+0.5
        nos=nos+1
    E = E + dE
plt.legend()
plt.show()