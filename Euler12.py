naturals = []
num =0
count =1
while True:
	num = num+count	
	count=count+1
	numoffactors=2
	for i in range(1,num/2):
		if num%i==0:
			numoffactors=numoffactors+1	
	if numoffactors>500:
		print num
		break
		
	
	
	

		