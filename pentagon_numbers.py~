import math
def pent(n):
	return n*(3*n-1)/2
def isPent(n):
	return ((math.sqrt(24*n+1)+1)/6).is_integer()
f=True
i=1

while(f):
	i+=1
	n=pent(i)
	for j in range(i-1,0,-1):
		m = pent(j)
		if isPent(n-m) and isPent(m+n):
			f=False
			print i, j, n, m, n-m
			break 	

