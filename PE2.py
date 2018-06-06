def make_fibin_list (max):
	fibin_list = [1, 2]
	previous = 1
	current = 2
	while current <= max:
		current, previous = current + previous, current
		fibin_list += [current]
	return fibin_list

def sum_evens(this_list):
	output = 0
	for i in this_list:
		if i%2 == 0:
			output += i
	return output

print (sum_evens(make_fibin_list(4000000)))