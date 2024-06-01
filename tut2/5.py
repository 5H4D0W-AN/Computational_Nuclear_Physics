import numpy as np
import math

E= 5.0* 1.60218e-13
A= 238
r1 = 1.07 * (A**0.33)* 1e-15
r2 = 8 * (A**0.33)* 1e-15
m= 6.644657230 * (10**(-27))
hcut= 1.05457182e-34

def V(x):
    k= 9e9
    z= 92
    esq= 2.56 * (10**(-38))
    return (k*2* z* esq)/(x)

def f(x):
    return math.sqrt(((2*m)/ (hcut**2)) * abs(V(x)-E))
 
 
def simpsons_( ll, ul, n ):
    h = ( ul - ll )/n
    res = 0
    for i in range(n+1):
        if i == 0 or i == n:
            res+= f(ll+i*h)
        elif i % 2 != 0:
            res+= 4 * f(ll+i*h)
        else:
            res+= 2 * f(ll+i*h)
        i+= 1
    res = res * (h / 3)
    return res


integ = simpsons_(r1, r2, 1000)
transmission_probab = math.exp(integ*(-2))
print("transmission_probabability= ", transmission_probab)