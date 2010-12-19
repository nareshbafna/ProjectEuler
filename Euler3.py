def isPrime(n):
	if n<=1:
		return False
	if n==2:
		return False
	if n%2==0:
		return False
	for i in range(3,n,2):		
		if n%i==0:
			return False
	return True

answer =0
import math
sqart =int(math.sqrt(600851475143))
for i in range(1,sqart):
	if (600851475143%i==0 and isPrime(i)):
		answer = i
		
print answer