# Let the "interesting substring" property discribed in the instructions be called "property a" 


def is_odd(n):
	if n%2 == 0:
		return False
	else:
		return True

def is_prime(number):
# returns the number if it is prime
	# print number
	for x in xrange(1, number):
		# print x
		if x > number/x:
			return True
		if x == number - 1:
			return True
		if x != 1 and number%x == 0:
			return False

def next_prime(n):
	# generates the next prime after n
	if is_odd(n):
		number = n + 2
	else:
		number = n +1

	while number <= n+100000000000:
		if is_prime(number):
			return number
		number += 2

def convert_to_int_list(list_of_strings):
	list_of_ints = []
	for elem in list_of_strings:
		number = int(elem)
		list_of_ints.append(number)
	return list_of_ints

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

	print list_to_return
	return list_to_return

# it would be cool to write a "generator function", like xrange, that produces primes.


def has_property_a(number):

	string_number = str(number)
	length = len(string_number)

	prime = 2
	# print range(length)
	for first_of_triplet in range(1,length-2):
		# print first_of_triplet
		# print first_of_triplet
		first = string_number[first_of_triplet]
		second = string_number[first_of_triplet+1]
		third = string_number[first_of_triplet+2]

		combined_number = int(first+second+third)
		print combined_number
		if not combined_number%prime == 0:
			return False

		prime = next_prime(prime)
		print "/"+ str(prime)

	return True 

# print has_property_a (1406357289)

# Step 1: Generate all pandigital numbers of 0to9 digits

def generate_all_x_y_pandigitals(x, y):
	to_digit = [i for i in range(x, y+1)]
	# list of digits from x to y
	list_of_string_permutations = generate_all_purmutations(to_digit)
	list_of_int_permutations = convert_to_int_list(list_of_string_permutations)
	# this makes all the pandigital numbers
	return list_of_int_permutations


# Step 2: For each number check if it has the interesting-substing-property

def filter_list_for_property_a(this_list):
	
	list_to_output = []

	for number in this_list:
		if has_property_a(number):
			list_to_output.append(number)

	return list_to_output


def the_answer_is():
	list_of_0_to_9_pandigitals = generate_all_x_y_pandigitals(0, 9)

	list_filitered_for_property_a = filter_list_for_property_a(list_of_0_to_9_pandigitals)
	
	print list_filitered_for_property_a
	sum_of_filtered = 0
	for number in list_filitered_for_property_a:
		sum_of_filtered += number

	return sum_of_filtered

print the_answer_is()
















