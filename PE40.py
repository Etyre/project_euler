def concatenate_integers (up_to_interger):
	string_concatenation = "0."
	for int in range(1, up_to_interger):
		string_int = str(int)
		string_concatenation += string_int
	return string_concatenation


def find_the_nth_decimal_digit (n, decimal_as_string):
	numbers_after_decimal = decimal_as_string.split(".")[1]
	numbers_after_decimal
	int_digit = int(numbers_after_decimal[n-1])
	return int_digit


def multiply_digits_of_a_string_using_only_indicies_that_go_up_by_10(index_of_last_digit_to_multiply):
	string = concatenate_integers(1000000)
	answer = 1
	i = 1

	while i <= index_of_last_digit_to_multiply:
		print i
		digit = find_the_nth_decimal_digit(i, string)
		print digit
		answer *= digit
		i *= 10
		print answer

	return answer

find_the_nth_decimal_digit (4, "0.3857290750289")

print multiply_digits_of_a_string_using_only_indicies_that_go_up_by_10(1000000)
