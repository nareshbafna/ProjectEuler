counter = []
for i in range(1,999999):
	num = i
	count =0
	while num!=1:
		count = count +1
		if num%2==0:
			num = num/2
		elif num%2!=0:
			num = num*3+1
	counter.append([i,count])
greater =0
number= 0
for x in counter:
	if x[1]>greater:
		greater = x[1]
		number=x[0]
print number

