import numpy as np
a = 7
j=2
l=3

def QSP(j):
	return -(0.5)*(0.6*(1.2*(a**(1/3)))**2)*(2*j-1)/(j+1)

def u(j, l, gl, gs):
	if(j>l):
		return (j-0.5)*gl + gs/2
	else:
		return (j/(j+1))*((j+1.5)*gl - gs/2)

gl = 1 #because p = 3
gs = 5.585

print("The Quadruple moment for 7Li: ", QSP(j))
print("Magnetic moment: ", u(j, l, gl, gs))
