import sys
n = int(input())
nn = n
ans1 = 1
ans2 = 1

# Loop to calculate the product of every second number down from n
while n > 0:
    ans2 *= n
    n -= 2
while nn > 0:
	ans1*=n
	n-=1
# Printing the result to standard output
print(ans1)
print('\n')
print(ans2)


