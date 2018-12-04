from functools import reduce
import re

# ~~~~~~~~~~~~~~~~~

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
			if hold == -1:
				hold = time
			else:
				if guard not in guards: guards[guard] = [0] * 60
				for i in range(hold, time + 1):
					guards[guard][i] += 1
				hold = -1

	mx1 = mn1 = mx2 = mn2 = 0
	g1 = g2 = None
	for k, v in guards.items():
		# calc
		s = sum(v)
		m = max(v)
		i = v.index(m)
		# 4.1
		if s > mx1:
			mx1 = s
			g1 = k
			mn1 = i
		# 4.2
		if m > mx2:
			mx2 = m
			g2 = k
			mn2 = i

	print('4.1:  guard {} * min {} = {}'.format(g1, mn1, int(g1) * mn1))

	# day 4.2
	print('4.2:  guard {} * min {} = {}'.format(g2, mn2, int(g2) * mn2))


# ~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
	main()

# concept:
#	> sort
#	> for each line
# 		> set guard, start time, or finish time and add to guard
#	> then just find maxes etc.