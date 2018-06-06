def find_digits(n):
	counter = 0
	while n >0:
		n = n /10
		counter += 1
	return counter




def find_index(number_of_digits, max):
	last = 1
	next_to_last = 0
	for x in range(2, max):
		index = x
		last, next_to_last = last + next_to_last, last
		print(x)
		print("last: "+str(last))
		print("next to last: "+ str(next_to_last))
		if find_digits(last) >= number_of_digits:
			print last
			print x
			break

# ^^ this works, but it's kind of inelegant. It works by starting the index at 2.

def find_index_elg(number_of_digits, max):
	last = 0
	next_to_last = 0
	current = 1
	for x in range(1, max):
		index = x
		print(x)
		print("current: "+str(current))
		print("last: "+ str(last))
		current, last,  = current + last, current
		if find_digits(last) >= number_of_digits:
			print current
			print x
			break

find_index_elg(1000, 5000)