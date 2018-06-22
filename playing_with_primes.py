

def make_primes(limit):
	if limit < 2:
		return []
	primes = [2]
	for i in range(2, limit):
		for x in primes:
			# print primes
			if x != 1 and i%x == 0:
				break
			if x == primes[-1] and i%x != 0:
				primes.append(i)
	return primes


# I should also reformat this /\ so that it takes advantage of the x must be smaller than (or = to) n/x insight.

def is_prime(number):
	# returns the number if it is prime
	for x in range(1, number):
		while x <= number/x:
			if x == number - 1:
				return number
			if x != 1 and number%x == 0:
				break
		return n

n = "[put a number here]"


make_primes(n)
print "done"


	# composites = []
	# primes = []
	# # Take a number i, greater than 1.
	# for i in range(2, limit):
	# # Compare i to each x in range(2, i).
	# 	for x in range(2, i):
	# # For each x, f i divides easily into x, add it to the list of composites...
	# 		if i%x == 0:
	# 			composites.append(i)
	# #...and take a new i.
	# 			break
	# # If  you've checked all the numbers up to i, without finding one that cleanly divides i,
	# # add i to the list of primes.
	# 	if i == x + 1:
	# 		primes.append(i)
	# # Take a new i.
	# print primes




# make_primes(8)



# make_primes(55)











