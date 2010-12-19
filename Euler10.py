def isPrime(n):
	if n<=1:
		return False
	if n==2:
		return True
	if n%2==0:
		return False
	for i in range(3,n,2):		
		if n%i==0:
			return False
	return True
	
n=2000000
sum = 0
#for i in range(2000000):
#	if isPrime(i):
#		sum = sum+i

bool=[]
for i in range(n):
	bool.insert(i,True)

bool[0]=False
bool[1]=False
import math
m = math.sqrt(n)
for i in range(2,m+1,1):
	if isPrime(i):
		for k in range(i*i,n,i):
			bool[k]=False
for i in range(n):
	if bool[i]==True:
		sum = sum+i
print sum