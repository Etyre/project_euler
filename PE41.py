
def generate_all_purmutations(list_of_numbers, permutation_peices):
	if len(list_of_numbers) == 0:
		return []

	full_list =[]

	for digit in list_of_numbers:
		new_list_of_numbers = list_of_numbers[:]
		new_list_of_numbers.remove(digit)

		new_permutation_peices = []

		for elem in permutation_peices:
			new_permutation_peices += str(digit)+elem

		if len(permutation_peices)== 0:
			new_permutation_peices = [str(digit)]
		print new_permutation_peices
		full_list += generate_all_purmutations(new_list_of_numbers, new_permutation_peices)
	return full_list






	# list_to_return =[]
	# if len(this_list) == 1:
	# 	return [this_list]
	# for i in this_list:
	# 	new_list = this_list[:]
	# 	new_list.remove (i)
	# 	print list_to_return
	# 	list_to_return.extend([i].extend(generate_all_purmutations(new_list)))
	# return list_to_return

test_list = [1,2,3,4]

print generate_all_purmutations(test_list, [])

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

