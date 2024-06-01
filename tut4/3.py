import numpy as np
import math

def cg_coeff(j1,m1,j2,m2,j,m):
    if m>j:
        return 0
     
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
        temp= math.factorial(int(j1-m1-s))*math.factorial(int(j2+m2-s))*math.factorial(int(j-j2+m1+s))*math.factorial(int(j-j1-m2+s))*math.factorial(int(j1+j2-j-s))*math.factorial(int(s))
        f3= f3 + ((-1)**s)/temp
    return f1*f2*f3


def ans(j, ja, jb, jc, jd, del_ab, del_cd,t):
    t1= 1/(2*(2*j+1))
    t2= math.sqrt(((2*ja+1)*(2*jb+1)*(2*jc+1)*(2*jd+1))/((1+del_ab)*(1+del_cd)))
    t3= pow(-1,jb+jd+2)*cg_coeff(jb, -0.5, ja, 0.5, j, 0) * cg_coeff(jd, -0.5, jc, 0.5, j,0)*(1- pow(-1, 2+j+t))
    t4= cg_coeff(jb, 0.5, ja, 0.5, j, 1)*cg_coeff(jd, 0.5, jc, 0.5, j, 1)*(1+ pow(-1,t))
    
    return t1*t2*(t3-t4)

def tbme(a,b,c,d):
    j1=0.5
    j2=0.5
    j3=0.5
    j4=0.5
    
    if a==1: 
        j1=1.5
    if b==1:
        j2=1.5
    if c==1:
        j3=1.5
    if d==1:
        j4=1.5
        
    delta_ab=0
    delta_cd=0
    
    if a==b:
        delta_ab=1
    if c==d:
        delta_cd=1
    
    equiv=0
    
    if delta_cd==1 or delta_ab==1:
        equiv=1
    
    jmin1= abs(j1-j2)
    jmax1= j1+j2
    
    jmin2= abs(j3-j4)
    jmax2= j3+j4
    
    jmin= int(max(jmin1, jmin2))
    jmax= int(min(jmax1, jmax2))

    
    for j in range(jmin,jmax+1,1):
        if equiv==1:
            t=0
            if j%2==0:
                t=1
            answer= ans(j, j1, j2, j3, j4, delta_ab, delta_cd, t)
            print(a,b,c,d,"  ", j, t, "  ",answer)
        else:
            t=0
            answer= ans(j, j1, j2, j3, j4, delta_ab, delta_cd, t)
            print(a,b,c,d,"  ", j, t, "  ",answer)
            t=1
            answer= ans(j, j1, j2, j3, j4, delta_ab, delta_cd, t)
            print(a,b,c,d,"  ", j, t, "  ",answer)      
    print("\n") 
print("a b c d    j t     V(sdi) \n")
abcd= ((1,1,1,1),
       (1,1,1,2),
       (1,1,2,2),
       (1,2,1,2),
       (1,2,2,2),
       (2,2,2,2))
        
for x in abcd:
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    
    tbme(a,b,c,d)