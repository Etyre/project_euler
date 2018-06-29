
import math

import string

file =  "p042_words.txt"


def nth_triangle_number(n):
	output = (n)*(n+1)/2
	return output


def is_triangle_number(number):
	# if the number given is a triangle number, the function returns True.
	double_the_number = number*2
	sqr_of_double_the_number = math.sqrt(double_the_number)
	round_sqr = int(math.ceil(sqr_of_double_the_number))

	for x in xrange(round_sqr, max(number, 10)):
		product = x*(x-1)
		if product == double_the_number:
			return True
		if product > double_the_number:
			return False


def make_letter_to_number_dictionary():
	dictionary = {}


letter_to_number_key = {letter: index for index, letter in enumerate(string.ascii_uppercase, start=1)}


def word_number(input_string):
	number = 0
	for letter in input_string:
		number += letter_to_number_key.get(letter, 0)

	return number


def how_many_words_have_triangle_numbers(input_file):
	with open(input_file, 'r') as contents:
		#READING
		my_list = []
		for item in contents:
    			my_list.append(item.strip().split(','))


	list_of_word_numbers = []
	list_of_triangle_number_words = []

	

	print my_list



	for word in my_list[0]:

		this_word_number = word_number(word)
		print this_word_number
		list_of_word_numbers.append(this_word_number)
		if is_triangle_number(this_word_number):
			list_of_triangle_number_words.append(word)

	print list_of_triangle_number_words
	# return list_of_triangle_number_words
	return len(list_of_triangle_number_words)


print how_many_words_have_triangle_numbers(file)





