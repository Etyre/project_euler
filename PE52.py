def digits_list(number):
	output = []
	for elem in str(number):
		output.append(int(elem))
	return output


def check_digits_match(first, second):
	digits_list_of_first = digits_list(first)
	print digits_list_of_first
	digits_list_of_second = digits_list(second)
	print digits_list_of_second

	if len(digits_list_of_first) != len(digits_list_of_second):
		return False

	# previously, this was a For Loop. But for some reason, it was selecting elements of the list out of order.
	# I don't know why.
	while len(digits_list_of_first) > 0:

		elem = digits_list_of_first[0]

		if elem not in digits_list_of_second:
			return False

		digits_list_of_first.remove(elem)
		digits_list_of_second.remove(elem)

		print digits_list_of_first
		print digits_list_of_second

	return True

def check_for_same_digits_of_multiples(number):
	for x in range(1, 7):
		if check_digits_match(number, number*x) == False:
			return False
	return True


def check_for_same_digits_of_multiples_up_to_n(number):
	for x in range(1, number):
		if check_for_same_digits_of_multiples(x) == True:
			return x
	return "no numbers less than or equal to "+str(number)+" have the relevent property."


print check_for_same_digits_of_multiples_up_to_n(200000)




