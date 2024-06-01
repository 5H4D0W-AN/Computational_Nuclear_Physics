import numpy as np
import matplotlib.pyplot as plt

a_v = 16
a_s = 20
a_c = 0.751
a_sym = 21.4
m_n = 939.565413
m_h = 938.272081
c = 3*(10**8)

def alpha(a):
    t1 = a_c*pow(a, 2/3)
    t2 = -1*(m_n-m_h)
    t3 = (4*a_sym)/a
    t4 = a_c/pow(a, 1/3)

    return (t1+t2)/(t3+t4)

def beta(a):
    t1 = 2*a_c*pow(a, 2/3)
    t2 = a_c*pow(a, 2/3)
    t3 = 12*a_sym
    return t1/(t2+t3)

def gamma(a):
    t1 = a_v
    t2 = 3*a_sym
    t3 = (-2/3)*a_s*pow(a, -1/3)
    t4 = (1/3)*a_c*pow(a, 2/3)
    t5 = 4*a_sym

    return (t1+t2+t3)/(t4+t5)

def alpha_neutro(a):
    t1 = a_v
    t2 = 3*a_sym
    t3 = (-2/3)*a_s*pow(a, -1/3)
    t4 = (a_c/3)*pow(a, 2/3)
    t5 = (1/3)*a_c*pow(a, 2/3)
    t6 = 4*a_sym
    return (t1+t2+t3+t4)/(t5+t6)


x1 = []
x2 = []
x3 = []
y1 = []
y2 = []
y3 = []

# beta stability line
for i in range(1, 251):
  temp = (i+alpha(i))/2
  x1.append(temp)
  y1.append(i - temp)

# proton drip line
for i in range(1, 251):
  temp = i*(1 + beta(i) - np.sqrt(pow(1+beta(i), 2) - gamma(i)))
  y2.append(temp)
  x2.append(i - temp)

# neutron drip line
for i in range(1, 251):
   x3.append(i*(1 - np.sqrt(1 - alpha_neutro(i))))
   y3.append(i*(np.sqrt(1 - alpha_neutro(i))))

plt.xlabel("N")  
plt.ylabel("Z")

plt.grid(True)
plt.plot(x1,y1, label = "Beta Stability Line")
plt.plot(x2,y2, label = "Proton Drip Line")
plt.plot(x3,y3, label = "Neutron Drip Line")  
plt.legend()  
plt.show()