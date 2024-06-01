import numpy as np
import math

def cg_coeff(K, I):
    j1= I
    j2= 2
    j= I-2
    m1= K
    m2= 0
    m= K

    d= j-j2+m1
    e= j-j1-m2

    smin = int(min(d,e))

    if smin > 0:
        smin=0
    else:
        smin = abs(smin)

    a= j1+j2-j
    b= j2+m2
    c= j1-m1

    smax= int(abs(min(a, b, c)))

    f1 = math.sqrt((math.factorial(int(j1+j2-j))*math.factorial(int(j+j1-j2))*math.factorial(int(j+j2-j1))*(j+j+1))/math.factorial(int(j1+j2+j+1)))
    f2 = math.sqrt(math.factorial(int(j+m))*math.factorial(int(j-m))*math.factorial(int(j1+m1))*math.factorial(int(j1-m1))*math.factorial(int(j2+m2))*math.factorial(int(j2-m2)))
    f3 = 0




    for s in range (smin, smax+1):
        temp= math.factorial(int(j1-m1-s))*math.factorial(int(j2+m2-s))*math.factorial(int(j-j2+m1+s))*math.factorial(int(j-j1-m2+s))*math.factorial(int(j1+j2-j-s))*math.factorial(s)
        f3= f3 + ((-1)**s)/temp

    return f1*f2*f3

def BE2(Qt, K, I):
    return 5/(16*np.pi)*(Qt**2)*(cg_coeff(K, I)**2)

i = [17/2, 21/2]
Q = [224, 202]
K = 2.5
for j in range(2):
    print(i[j], "->", i[j]-2, " : ", BE2(Q[j], K, i[j]))
