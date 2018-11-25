#	PLAN: 

# 1. make_prime function

# 2. All templates for number of length n. 
# (templates for 1: 0, 1.          2: 00, 01, 10, 11)

#  	3. loop through templates 
# 		loop through digits
# 			and replace every digit coresponding to a 1 on the template with the digit.
#			check if the result is prime, if so, save. 
#			count the number of savaed primes.


import copy


#from PE51.v1
def is_prime(number):
	# returns the number if it is prime
	for x in range(1, number):
			if x == number - 1:
				return True
			if x != 1 and number%x == 0:
				break

# from PE41
def make_primes2(limit):
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


def make_templates(n):
	if n <= 0:
		return []
	else: 
		templates = ["0", "1"]
		
		counter = 1

		while counter < n:
			add_zeros = []
			for elem in templates:
				add_zeros.append(elem + "0")

			add_ones = []
			for elem in templates:
				add_ones.append(elem + "1")

			print templates
			templates = add_zeros + add_ones			
			counter += 1
	print " "
	return templates

print make_templates(3)

def find_prime_value_family (order_of_magnitude, required_family_size):
	limit_number = 10 ** order_of_magnitude 
	list_of_primes = make_primes2(limit_number)

	number_of_digits = order_of_magnitude
	templates = make_templates(number_of_digits)

	for prime in list_of_primes:
		string_prime = str(prime)

		for template in templates:
			primes_that_match_the_template = []

			for digit in range(10):
				new_string_for_alteration = copy.copy(string_prime)

				for i in range(len(template)):
					print i

					if template[i] == 1:
						new_string_for_alteration[i] == digit

				# for i in len(new_string_for_alteration):
				# 	if new_string_for_alteration[i] == 0:
				# 		new_string_for_alteration = new_string_for_alteration[1:]
				# 	else:


				altered_number = int(new_string_for_alteration)

				if altered_number in list_of_primes and altered_number not in primes_that_match_the_template:
					primes_that_match_the_template.append(altered_number)

			if primes_that_match_the_template != []:
				print primes_that_match_the_template
			if len(primes_that_match_the_template) >= required_family_size:
				return primes_that_match_the_template

	return "no numbers under "+ str(limit_number)+ " meet the criteria."





def generate_variants_that_that_match_the_template(input_number, template):

	list_of_variants = []
	list_input_number = list(input_number)

	for digit in range(10):

		for i in range(len(template)):
			print i

			if template[i] = 1:

				new_list_number[i] = digit







