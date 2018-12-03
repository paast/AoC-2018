from collections import Counter

# returns tuple boolean (found_2, found_3)
def reps(id):
	count = Counter(id)
	return (2 in count.values(), 3 in count.values())

def find_pair(list):

	def test_pair(a, b):
		mismatch = 0
		chars = []
		for pos in range(len(a)):
			if (a[pos] != b[pos]):
				mismatch += 1
				if mismatch > 1:
					return False
			else:
				chars.append(a[pos])
		return chars


	l = len(list)
	for a in range(l):
		for b in range(a + 1, l):
			test = test_pair(list[a], list[b])
			if test: return test


def main():
	
	# load dataset
	with open('2.txt', 'r') as f:
		idlist = [line.strip('\n') for line in f.readlines()]

	# day 2.1
	c2 = c3 = 0
	for id in idlist:
		 r = reps(id)
		 c2 += r[0]
		 c3 += r[1]

	print(c2 * c3)

	# day 2.2
	print(''.join(find_pair(idlist)))



# ~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
	main()