import numpy as np

def f(x):
	return x*x*(np.exp(-x*x))

def simpson(a, b, n):
	h = (b-a)/n;
	ret = 0;
	for i in range(0, n):
		if(i==0):
			ret += f(a+i*h)
		elif i%2==0:
			ret += 2*f(a+i*h)
		else:
			ret += 4*f(a+i*h)
	ret = (ret*h)/3
	return ret

ans = simpson(0, 2, 100000)
print("Answer using simpson method: ", ans)