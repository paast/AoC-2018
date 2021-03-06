
def main():

	# load dataset
	with open('1.txt', 'r') as f:
		flist = [int(x) for x in f.readlines()]

	# day 1.1
	print(sum(flist))

	# day 1.2
	count = 0
	fsum = 0
	fset = set({})
	l = len(flist)

	while True:
		fsum += flist[count]
		
		if (fsum in fset):
			print(fsum)
			break
		else:
			fset.add(fsum)
		
		count += 1
		if (count >= l): count %= l


# ~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
	main()