
def generate_all_purmutations(list_of_digits):
	list_to_return = []
	# print list_of_digits

	if len(list_of_digits)== 1:
		string_digit = str(list_of_digits[0])
		sting_digit_in_list = [string_digit]
		
		digit = list_of_digits[0]
		return string_digit

	for digit in list_of_digits:
		minus_digit_list = list_of_digits[:]
		minus_digit_list.remove(digit)
		# print minus_digit_list

		list_of_permumtations_without_the_digit = generate_all_purmutations(minus_digit_list)
		# print list_of_permumtations_without_the_digit
		for elem in list_of_permumtations_without_the_digit:
			#the element should be a string here
			new_item = elem + str(digit)
			list_to_return.append(new_item)

	return list_to_return

def convert_to_int_list(list_of_strings):
	list_of_ints = []
	for elem in list_of_strings:
		number = int(elem)
		list_of_ints.append(number)
	return list_of_ints

def is_prime(number):
	# returns the number if it is prime
	for x in range(1, number):
			if x == number - 1:
				return True
			if x != 1 and number%x == 0:
				return False

def find_largest_pandigital_prime():
	limit = 10
	# we're going to try nine-digit numbers first, so we put one more than 9 as the imput to the range function
	while limit > 0:

		to_digit = [i for i in range(1, limit)]

		list_of_string_permutations = generate_all_purmutations(to_digit)
		list_of_int_permutations = convert_to_int_list(list_of_string_permutations)
		list_of_int_permutations.sort(reverse = True)

		for number in list_of_int_permutations:
			if is_prime(number):
				return number

		limit -= 1



find_largest_pandigital_prime()	





	# list_to_return =[]
	# if len(this_list) == 1:
	# 	return [this_list]
	# for i in this_list:
	# 	new_list = this_list[:]
	# 	new_list.remove (i)
	# 	print list_to_return
	# 	list_to_return.extend([i].extend(generate_all_purmutations(new_list)))
	# return list_to_return




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

