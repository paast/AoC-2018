
def main():
	
	# load dataset
	with open('4.txt') as file:
		lines = file.readlines()

	# day 4.1
	lines.sort()
	guards = {}
	guard = None
	hold = -1
	for line in lines:

		time = int(line[15:17])
		test = line[19:-1].split('Guard #')

		# guard line
		if (len(test) > 1):
			guard = test[1].split(' ')[0]

		# sleep/wake line
		else:
			# sleep
			if hold == -1:
				hold = time
			# wake
			else:
				if guard not in guards:
					guards[guard] = [0] * 60

				for i in range(hold, time + 1):
					guards[guard][i] += 1

				hold = -1

	max1 = minute1 = max2 = minute2 = 0
	guard1 = guard3 = None
	for k, v in guards.items():

		# calc
		s = sum(v)
		m = max(v)
		i = v.index(m)

		# 4.1
		if s > max1:
			max1 = s
			guard1 = k
			minute1 = i
			
		# 4.2
		if m > max2:
			max2 = m
			guard3 = k
			minute2 = i

	print('4.1:  guard {} * min {} = {}'.format(guard1, minute1, int(guard1) * minute1))

	# day 4.2
	print('4.2:  guard {} * min {} = {}'.format(guard3, minute2, int(guard3) * minute2))


# ~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
	main()

# concept:
#	> sort
#	> for each line
# 		> set guard, start time, or finish time and add to guard
#	> then just find maxes etc.