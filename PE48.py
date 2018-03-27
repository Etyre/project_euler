def sum_of_self_powers (end):
	total = 0
	for i in range(1, end+1):
		a = i**i
		total += a

	return total

def number_of_digits(number):
	n = number
	counter = 0
	if n == 0:
		return 1
	while n > 0:
		n = n/10 
		counter += 1
	return counter

print number_of_digits(0)



def last_ten_digits(number):

	print number%10000000000

last_ten_digits( sum_of_self_powers(1000))
