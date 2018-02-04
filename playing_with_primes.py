
def make_primes(limit):
	composites = []
	primes = []
	for i in range(2, limit):
		for x in range(2, i):
			if x == i - 1:
				primes.append(i)
			if i%x == 0:
				composites.append(i)
				break
	print primes





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


make_primes(55)











