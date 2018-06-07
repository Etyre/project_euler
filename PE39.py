
import math

# the method of generating pythagorean triples and then checking their perimeters

# the method of picking starting from the perimeter, and then checking the other
def gernerate_right_integer_triangles(perim):

	min_hypotanus_limit = perim * 0.40
	max_hypotanus_limit = perim / 2
	hypotanus = int(math.ceil(min_hypotanus_limit))

	list_of_triplets = []

	while hypotanus < max_hypotanus_limit:
		rest = perim - hypotanus
		rest_midpoint = rest//2
		for leg_1 in range(1, int(rest_midpoint)+1):
			leg_2 = int(rest - leg_1)
			if leg_1**2 + leg_2**2 == hypotanus**2:
				list_of_triplets.append([hypotanus, leg_1, leg_2])
		hypotanus += 1

	return list_of_triplets

def find_perimeter_of_most_triplets(upper_limt):
	best_perimeter = 0
	count_of_best_perimeter = 0

	for perimeter in range(1, upper_limt):
		list_of_triplets = gernerate_right_integer_triangles(perimeter)
		print "current perimeter: "+str(perimeter)
		print list_of_triplets
		if len(list_of_triplets) > count_of_best_perimeter:
			best_perimeter = perimeter
			count_of_best_perimeter = len(list_of_triplets)
			print list_of_triplets
	return best_perimeter

print find_perimeter_of_most_triplets(1000)