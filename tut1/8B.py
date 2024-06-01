import numpy as np
import math

j1= 0.5
j2= 0.5
j= 1
m1= 0.5
m2= 0.5
m= 0

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
f2 = math.sqrt(math.factorial(j+m)*math.factorial(j-m)*math.factorial(int(j1+m1))*math.factorial(int(j1-m1))*math.factorial(int(j2+m2))*math.factorial(int(j2-m2)))
f3 = 0

for s in range (smin, smax+1):
    temp= math.factorial(int(j1-m1-s))*math.factorial(int(j2+m2-s))*math.factorial(int(j-j2+m1+s))*math.factorial(int(j-j1-m2+s))*math.factorial(int(j1+j2-j-s))*math.factorial(s)
    f3= f3 + ((-1)**s)/temp

print("f1: ", f1)
print("f2: ", f2)
print("f2: ", f3)
print("C : ", f1*f2*f3)