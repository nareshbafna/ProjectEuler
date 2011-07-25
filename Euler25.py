fibs = []
fibs.append(1)
fibs.append(1)
num = fibs[0]+fibs[1]
i =2
while True:
	fibs.append(fibs[i-1]+fibs[i-2])
	#print fibs[i], len(str(fibs[i]))
	if len(str(fibs[i]))==1000: 
		print i
		break
	i=i+1
