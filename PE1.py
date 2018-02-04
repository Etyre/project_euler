

def sum_mults_of_3_and_5(upper_limit):
	answer = 0
	for i in range(upper_limit):
		if i%3 == 0 or i%5 ==0:
			answer += i

	print answer


sum_mults_of_3_and_5(1000)



