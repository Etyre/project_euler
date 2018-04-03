


# An alorithim:

# 1. make all the primes of n digits, and store them in current_primes

# 2. take the first of the list, and generate all the permutations



def find_digits(n):
	counter = 0
	while n >0:
		n = n /10
		counter += 1
	return counter

def find_permuatations(n, starter_list=[[]]):
	# this function takes some natural number, 
	# starter list should be a list of lists
	if n == 0:
		return starter_list

	else:
		output = []
		for elem in starter_list:
			# each elem should be a list
			add_zero = elem + [0]
			add_one = elem +[1]

			output.append(add_zero)
			output.append(add_one)

		return find_permuatations(n-1, output)

def is_prime(number):
	# returns the number if it is prime
	for x in range(1, number):
			if x == number - 1:
				return True
			if x != 1 and number%x == 0:
				break

def make_char_list_from_string(my_string):
	output_list = []

	for char in my_string:
		output_list.append(char)

	return output_list


def make_string_from_char_list(my_char_list):
	output_string = ""

	for char in my_char_list:
		output_string += char

	return output_string


def replace_the_ons_with_digit(number, sequence, digit):
#sequence is a list of ones and zeros digit is an integer,
# the function returns an integer
	#turn the number into a list of strings.
	string_number = str(number)
	char_list_number = make_char_list_from_string(string_number)

	# turn the digit into a string
	string_digit = str(digit)

	for i in range(len(char_list_number)):
		if sequence[i] == 1:
			char_list_number[i] = string_digit

	# make the number into an integer again

	new_string = make_string_from_char_list(char_list_number)
	new_int = int(new_string)

	return new_int


def generate_variations_and_check_if_prime(n, possible_permutations):
	

	for given_permuation_seqence in possible_permutations: #picking the permutation sequence

		primes_that_share_a_permutation_sequence = []

		for digit in range(10): # picking the digit

			# replace the "on"s with a given digit
			current_variation = replace_the_ons_with_digit(n, given_permuation_seqence, digit)

			if is_prime(current_variation) == True and current_variation not in primes_that_share_a_permutation_sequence:
				primes_that_share_a_permutation_sequence.append(current_variation)

		# these two lines could be constructed as a while loop instead.
		if len(primes_that_share_a_permutation_sequence) >= 8:
			return primes_that_share_a_permutation_sequence
			
print find_digits(11)

print find_permuatations(find_digits(11))

print generate_variations_and_check_if_prime(11, find_permuatations(find_digits(11)))

# Another algorthim:

# n = 1
# prime_family = []
# while len(prime_family) < 8:

# # Make a prime
# 	for x in range(1, n):
# 			if x == n - 1:
# 				# if it's a prime: 
# 				# 2. check if it has duplicate digits
				

# 				# 3. 

# 				# 4.







# 			if x != 1 and i%x == 0:
# 				break



# def find_modifications(number):
# 	digits = find_digits(number)

# 	generate_perm(digits)




# def generate_digit_perm(number):
# 	digits = find_digits

# 	if digits == 0:
# 		return [[0], []]
# 	else:
# 		return [[].append(generate_digit_perm(number-1)), [digits].append(generate_digit_perm(n-1))]


# def binary_perm(n):
# 	list_of_perm = []

# 	def inner_binary_perm(list_so_far, n):
# 		if n = 0:
# 			return [list_so_far.append(1), list_so_far.append(0)]
# 		else:
# 			return [list_so_far.append()


# e

# 3. outer loop: change each digit in turn.

# 4. inner loop: change each second digit in turn

# 5. check if each one is prime. if it is, add it to the list of primes.
