def is_prime(number):
# returns the number if it is prime
	print number
	for x in xrange(1, number):
		print x
		if x > number/x:
			return True
		if x == number - 1:
			return True
		if x != 1 and number%x == 0:
			return False
		

print is_prime(98765432)