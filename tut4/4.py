import numpy as np
import math
import matplotlib.pyplot as plt

def factorial(n):
    if (n<=1):
        return 1
    else:
        return n*factorial(n-1)
    


def cg_coef(j1, m1, j2, m2, j, m):
    d = j - j2 + m1
    e = j - j1 - m2
    smin = int(min(d,e))

    if smin <= 0:
        smin = abs(smin)
    else:
        smin = 0

    a = j1 + j2 - j
    b = j2 + m2
    c = j1 - m1
    smax = int(abs(min(a, min(b,c))))

    n1 = factorial(j1+j2-j)*factorial(j+j1-j2)*factorial(j+j2-j1)*(2*j +1)
    d1 = factorial(j1+j2+j+1)
    f1 = math.sqrt(n1/d1)

    f2 = math.sqrt(factorial(j+m)*factorial(j-m)*factorial(j1+m1)*factorial(j1-m1)*factorial(j2+m2)*factorial(j2-m2))
    f3 = 0

    for s in range(smin, smax+1):
        f3 = f3 + ((-1)**s)/(factorial(j1-m1-s)*factorial(j2+m2-s)*factorial(j-j2+m1+s)*factorial(j-j1-m2+s)*factorial(j1+j2-j-s)*factorial(s))

    # print(f1*f2*f3)
    return f1*f2*f3





a = 80
def h_omega(delta):
    f = pow((1 - ((4/3)*delta))*((1 + ((2/3)*delta))**2), -1/6)
    h_omeg = 41*pow(a, -1/3)*f
    return 1 #h_omeg
 




h_omega00 = 41*pow(a, -1/3)
kappa = 0.05
c = -2*kappa*h_omega00

miu = [0.0, 0.0, 0.0, 0.35, 0.625, 0.63, 0.448, 0.434]

    
def delta_n(N, N1):

    delta_n = 0
    if N==N1:
        delta_n = 1
    return delta_n


def h_delta(delta, rs, yy):

    t = -delta*h_omega(delta)*(4/3)*np.sqrt(np.pi/5)*rs*yy
    return t

def h00(N, N1, l, l1, lmbda, lmbda1, sigma, sigma1, delt):

    t = (N + 3/2)*h_omega(delt)*delta_n(N, N1)*delta_n(l, l1)*delta_n(lmbda, lmbda1)*delta_n(sigma, sigma1)
    return t

def l_square(N, N1, l, l1, lmbda, lmbda1, sigma, sigma1):

    t = l*(l+1)*delta_n(N, N1)*delta_n(l, l1)*delta_n(lmbda, lmbda1)*delta_n(sigma, sigma1)
    return t

def ls(N, N1, l, l1, lmbda, lmbda1, sigma, sigma1):

    t = 0.5*np.sqrt((l-lmbda)*(l+lmbda+1))*delta_n(lmbda, lmbda1)*delta_n(sigma-1, sigma1) + 0.5*np.sqrt((l+lmbda)*(l-lmbda+1))*delta_n(lmbda-1, lmbda1)*delta_n(sigma+1, sigma1) + lmbda*sigma*delta_n(lmbda, lmbda1)
    return t

def r_square(N, N1, l, l1, lmbda, lmbda1, sigma, sigma1):

    t = np.sqrt((N-l+2)*(N+l+1))*delta_n(l-2, l1) + (N + 3/2)*delta_n(l, l1) + np.sqrt((N-l)*(N+l+3))*delta_n(l+2, l1)
    return t


def y20(N, N1, l, l1, lmbda, lmbda1, sigma, sigma1):
    
    t = np.sqrt((5*(2*l + 1))/(4*np.pi*(2*l1 + 1)))
    t = t * cg_coef(l, lmbda, 2, 0, l1, lmbda1)
    t = t * cg_coef(l, 0, 2, 0, l1, 0)

    return t



def hamiltonian(N, N1, l, l1, lmbda, lmbda1, sigma, sigma1, delta):
    
    h0 = h00(N, N1, l, l1, lmbda, lmbda1, sigma, sigma1, delta)
    
    rs = r_square(N, N1, l, l1, lmbda, lmbda1, sigma, sigma1)
    yy = y20(N, N1, l, l1, lmbda, lmbda1, sigma, sigma1)
    hd = h_delta(delta, rs, yy)

    hls = ls(N, N1, l, l1, lmbda, lmbda1, sigma, sigma1)

    hll = l_square(N, N1, l, l1, lmbda, lmbda1, sigma, sigma1)
    
    mm = miu[int(N)]
    d = (c/2)*mm
    t = h0 + hd + c*hls + d*hll
    return t


print(hamiltonian(0, 0, 0, 0, 0, 0, 1, 1, -1))
print(hamiltonian(1, 1, 1, 1, 0, 0, 1, 1, -1))





N = []
L = []
lamda = []
omega = []
E=np.zeros((81,121))
d= np.arange(-0.4,0.41,1)
kappa=np.full((8),0.05)
mu=np.array([0.0,0.0,0.0,0.35,0.625,0.63,0.448,0.434])
co=0

for n in range(0,4,2):
    for om in range(1,n+2,2):
        #print(om)
        basis=[]
        for l in range(n,-1,-4):
            for lam in range(-l,l+1,2):
                sigma = om - lam
                if (abs(sigma) == 1):
                    basis.append([n,l,lam,sigma,om])
  
                    print('Basis elements:- ',basis)
                    #print('Length of basis:- ',len(basis))
        N_ = (len(basis))
        #print(N_)
        de = 0
        #print(N_)
        for delta in d:
            fdel=(((1+(0.67)*delta)**2)*(1-(1.33)*delta))**(-0.0167)
            hw00=1
            hw0=hw00*fdel
            C=-2.0*kappa[n//2]
            D=0.5*C*mu[n//2]
            H = np.zeros((N_,N_))
            for i in range(N_):
                n = basis[i][0]
                li = basis[i][1]
                Vi = basis[i][2]
                Si = basis[i][3]
                for j in range(i,N_):
                    lj = basis[j][1]
                    Vj = basis[j][2]
                    Sj = basis[j][3]
                    hdel= hamiltonian(n/2, n/2, li/2, lj/2, Vi/2, Vj/2, Si/2, Sj/2, delta)
                    # print(n,n, li, lj,Vi, Vj, Si, Sj, delta, hdel)
                    H[i,j] += hdel
                    H[j,i] = H[i,j]
            print("hamiltonian=",H)
            e_val,e_vec=np.linalg.eig(H)
            idx = e_val.argsort()[::1]
            e_val = e_val[idx]
            e_vec = e_vec[:,idx]
            #print('e_val',e_val)      
            E[de,0]=delta
            for i in range(0,N_):
                E[de,1+co+i]=e_val[i]      
            de += 1
            #print('de',de)
        co = co+N_        
        #print('co',co)    

print(E)

for e in E:
    print(E)
    
    

plt.figure(figsize = (12,14),dpi = 50)
plt.axvline(x = 0,ymin = 0,ymax = 1,c = 'k')
for i in range(1,len(E[0])):
    plt.plot(E[:,0],E[:,i])

plt.ylim(1,5)
# plt.xlim(-0.4,0.4)

plt.xlabel('$\delta$')
plt.ylabel('E($\hbar\omega_o$)')
plt.title('Nilson Model')
plt.show()
