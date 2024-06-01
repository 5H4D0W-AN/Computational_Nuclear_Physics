import numpy as np

A = 36

def b(hw):
	return 197.33*(940*hw)**(-0.5)

hw1 = 41*(A**(-1/3))
hw2 = 45*(A**(-1/3)) - 25*(A**(-2/3))

print("Oscillator length parameter, b, from 1st equation: ", b(hw1))
print("b, from 2nd equation                             : ", b(hw2))
