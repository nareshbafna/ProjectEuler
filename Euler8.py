f= open('Problem8Input.txt')
s= f.read().strip().replace('\n','').replace('\r','')
answer =0
for i in range(len(s)-4):
	if (int(s[i])*int(s[i+1])*int(s[i+2])*int(s[i+3])*int(s[i+4])>answer):
		answer =int(s[i])*int(s[i+1])*int(s[i+2])*int(s[i+3])*int(s[i+4])
print answer