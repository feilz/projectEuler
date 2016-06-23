import math
def isTri(n):
	return ((-1+math.sqrt(8*n+1))/2).is_integer()
def isPent(n):
	return ((1+math.sqrt(24*n+1))/6).is_integer()
def isHex(n):
	return ((1+math.sqrt(8*n+1))/4).is_integer()
f=True
i = 285
#print isTri(i), isPent(i), isHex(i)
cnt=0
def tri(n):
	return (n*(n+1))/2
while f:
	i+=1
	n = tri(i)
	if isPent(n) and isHex(n):
		print n
		f=False
