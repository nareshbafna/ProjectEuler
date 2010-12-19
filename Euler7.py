def isPrime(n):
	if n<=1:
		return False
	if n==2:
		return True
	if n%2==0:
		return False
	import math
	m = math.sqrt(n)
	for i in range(3,n,2):
		if(n%i==0):
			return False
	return True
	

count =0
number =0
while count!=10001:
	number = number+1
	if isPrime(number):		
		count= count+1		
print number

	
	