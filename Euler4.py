def isPalindrome(s):
	for i in range(len(s)/2):
		if s[i]!=s[len(s)-i-1]:
			return False
	return True

answer =0
for i in range(100,1000):
	for k in range(100,1000):	
		if isPalindrome(str(i*k)):
			if i*k > answer:
				answer = i*k			
print answer
	
	