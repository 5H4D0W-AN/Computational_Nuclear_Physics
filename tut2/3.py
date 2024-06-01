import numpy as np
import matplotlib.pyplot as plt

coef = [15.75, 17.80, 23.70, 0.71, 33.50]
def func(a, z):
    li = []
    c1 = a
    c2 = -1*pow(a, 2/3)
    c3 = -1*pow((a-2*z),2)/a
    c4 = -1*pow(z,2)/pow(a,1/3)
    c5 = 0
    if a%2==0:
        if z%2==1:
            c5 = -1*pow(a, -0.75)
        else: 
            c5 = pow(a, -0.75)
            
    li.append(c1)
    li.append(c2)
    li.append(c3)
    li.append(c4)
    li.append(c5)
    
    return li

def binding_energy(a, z, coef):
    l = func(a,z)
    t1 = coef[0]*l[0]
    t2 = coef[1]*l[1]
    t3 = coef[2]*l[2]
    t4 = coef[3]*l[3]
    t5 = coef[4]*l[4]
    
    return t1+t2+t3+t4+t5

x = []
y = []
for i in range(1, 251):
  x.append(i)
  y.append(binding_energy(i, i/2, coef)/i)

plt.xlabel("Mass Number (A)")  
plt.ylabel("BE per nucleon (MeV)")
plt.title("Binding Energy per Nucleon")
plt.grid(True)
plt.plot(x,y)    
plt.show()