f= open('Problem13Input.txt')
s = f.read().replace('\n','').replace('\r','')
numbers=[]
count=0
sum=0
for i in range(100):
	num=int(s[count:count+12])
	count = count+50
	sum=sum+num
print str(sum)[0:10]
