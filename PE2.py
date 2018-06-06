def make_fibin_list (max):
	fibin_list = [1, 2]
	previous = 1
	current = 2
	while current <= max:
		current, previous = current + previous, current
		fibin_list += [current]
		print fibin_list


make_fibin_list(10)

