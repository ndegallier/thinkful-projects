# Fizz Buzz Program

n = 100
print "Fizz Buzz counting up to {}.".format(n)

i = 0
Numbers = []

while i + 1 <= n:
	i = i + 1
	
	if i % 3 == 0 and i % 5 == 0:
		print "Fizz Buzz"
		
	elif i % 3 == 0 and (i % 5 == 0) == False:
		print "Fizz"
		
	elif (i % 3 == 0) == False and i % 5 == 0:
		print "Buzz"
	
	else:
		print i