import numpy as np

def func (A, Z):
    l= []
    a= A
    b= -1*(A** 0.66667)
    c= -1*((A-2*Z)**2)/A
    d= -1*(Z*Z)/ (A**0.3333)
    e=0
    if A%2==0:
        e= 1/ (A**0.75)
        if Z%2==1:
            e= e*(-1) 
    
    l.append(a)
    l.append(b)
    l.append(c)
    l.append(d)
    l.append(e)
    return l

def bind_energy(A, Z, l):
    a= func(A,Z)
    e=0
    e += a[0]*l[0]
    e += a[1]*l[1]
    e += a[2]*l[2]
    e += a[3]*l[3]
    e += a[4]*l[4]
    return e
    
l1= func(10,4)
l2= func(14,6)
l3= func(18,8)
l4= func(26,12)
l5= func(30,14)

m1= []
m1.append(l1)
m1.append(l2)
m1.append(l3)
m1.append(l4)
m1.append(l5)

m2= [6.498, 7.520, 7.767, 8.334, 8.521]

ans= np.linalg.solve(m1,m2)
print(ans)

eBe= bind_energy(10, 4, ans)
print("Be ", eBe)

eC= bind_energy(14, 6, ans)
print("C ", eC)

eO= bind_energy(18, 8, ans)
print("O ", eO)

eMg= bind_energy(26, 12, ans)
print("Mg ", eMg)

eSi= bind_energy(30, 14, ans)
print("Si ", eSi)
