n={}
n[0]=0
n[1]=1
count =1
answer =0
while True:	
	count = count+1
	n[count]=n[count-1]+n[count-2]
	if n[count]%2==0:
		answer = answer+ n[count]
	if n[count]>4000000:
		break
print answer