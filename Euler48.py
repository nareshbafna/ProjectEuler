sum=0
for i in range(1,1001):	
	num=1
	for k in range(i):
		num=num*i	
	sum=sum+num
print str(sum)[-10:]