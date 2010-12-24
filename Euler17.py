mappings = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:7,1000:8,0:0}

def getScore(number):
	if number<=20:
		return mappings[number]
	elif number > 20 and number<100:
		return mappings[(number/10)*10]+ mappings[number%10]
	elif number>=100 and number<1000:		
		score=mappings[number/100]+mappings[100]
		hundreth = number%100
		if hundreth!=0:
			if hundreth<21:
				score = score + mappings[hundreth] + 3
			else:
				score = score + mappings[(hundreth/10)*10] + mappings[hundreth%10]+3
		return score
	elif number==1000:
		return mappings[1]+mappings[1000]
sum=0
for i in range(1,1001):
	sum = sum + getScore(i)
print sum
print getScore(342)
print getScore(115)
#ninehundredandone
#ninehundredandninetynine



