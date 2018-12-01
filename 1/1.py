
# 1.1

# input = list(map(lambda x: int(x), open('1.txt').readlines()))

# sum = 0
# for num in input:
# 	sum += num

# print(sum)


# # 1.2

# fset = set({})
# dupe = None
# count = sum = 0
# l = len(input)
# while (dupe == None):

# 	if (count >= l):
# 		count %= l

# 	sum += input[count]
# 	if (sum in fset):
# 		dupe = sum
# 		break
# 	else:
# 		fset.add(sum)

# 	count += 1

# print(len(fset))
# print(dupe)


def main():

	with open('1.txt', 'r') as f:
		flist = [int(x) for x in f.readlines()]

	# day 1.1
	print(sum(flist))

	# day 1.2
	c = s = 0
	fset = set({})
	l = len(flist)
	while True:
		s += flist[c]
		if (s in fset):
			print(s)
			break
		fset.add(s)
		c += 1
		if (c >= l):
			c %= l


# ~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
	main()