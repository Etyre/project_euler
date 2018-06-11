






# This\/ version works, but it's not very practicable, because it takes too long to run 

# def make_primes(limit):
# 	if limit < 2:
# 		return []
# 	primes = [2]
# 	for i in range(2, limit):
# 		for x in primes:
# 			# print primes
# 			if x != 1 and i%x == 0:
# 				break
# 			if x == primes[-1] and i%x != 0:
# 				primes.append(i)
# 	return primes

# def check_if_pandecimal(input):
# 	n = len(str(input))
# 	# make the list of digits
# 	list_of_digits = []
# 	for digit in range(1, n+1):
# 		list_of_digits.append(digit)
# 	# make the list form of the number:
# 	number_as_list = []
# 	for index in range (0, n):
# 		number_as_list.append(int(str(input)[index]))

# 	# matching the lists to eachother
# 	for digit in list_of_digits:
# 		try: 
# 			number_as_list.remove(digit)
# 		except ValueError:
# 			return 0
# 	return 1
	

# def find_largest_prime_pandecimal(limit):
# 	list_of_primes = make_primes(limit)
# 	list_of_primes.reverse()

# 	for prime in list_of_primes:
# 		if check_if_pandecimal(prime) == 1:
# 			return prime
# 	return "something went wrong"

# print find_largest_prime_pandecimal(999999999)

