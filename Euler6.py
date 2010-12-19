sumofsquare=0
squareofsum=0
for i in range(101):
	sumofsquare = sumofsquare +i*i
	squareofsum = squareofsum+i
print str(squareofsum*squareofsum - sumofsquare)
