# https://projecteuler.net/problem=53

def factorial(number):
	if number == 0:
		return 1

	output = 1

	for x in range(1, number+1):
		output *= x

	return output


def select_r_from_n(r, n):
	if r > n:
		print "r can't be greater than n"
	output = factorial(n) / (factorial(r) * factorial(n-r))

	return output


def how_many_numbers_of_combinations_are_greater_than_a_million(max_number):
	counter = 0
	for n in range(1, max_number+1):
		for r in range(1, n):
			if select_r_from_n(r, n) > 1000000:
				counter += 1
	return counter

print how_many_numbers_of_combinations_are_greater_than_a_million(100)

