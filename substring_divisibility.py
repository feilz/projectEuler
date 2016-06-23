import math
from itertools import permutations

div=[2,3,5,7,11,13,17]

obj = permutations(range(0,10))
total=0
def addup(a,b,c):
	return a*100+b*10+c
for x in obj:
	for i in range(7):
		if addup(x[i+1],x[i+2],x[i+3])%div[i]==0:
			if i==6:
				total+=x[0]*1000000000+100000000*x[1]+10000000*x[2]+1000000*x[3]+100000*x[4]+10000*x[5]+1000*x[6]+100*x[7]+10*x[8]+x[9]
		
		else:
			break
print total
