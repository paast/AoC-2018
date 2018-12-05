import string
from functools import reduce


def is_pair(a, b):	
	"""Tests if two characters are the same letter
	but opposite capitalization"""

	if (not a.isalpha() or not b.isalpha()):
		return False

	test = ord(a) - ord(b)
	if (test == 32 or test == -32):
		return True
	
	return False

def polymerize(polymer):
	passed = ""
	skip = False

	for index, monomer in enumerate(polymer):
		if (skip):
			skip = False
			continue

		if (is_pair(passed[-1:], monomer)):
			passed = passed[:-1]
		elif (is_pair(monomer, polymer[index + 1])):
			skip = True
		else:
			passed += monomer

	return passed

def main():

	# load dataset
	with open("polymer.txt") as file:
		polymer = file.read()

	# 5.1
	new_polymer = polymerize(polymer)

	print('5.1:  start = {},  end = {}'.format(len(polymer), len(new_polymer)))

	# 5.2
	lowest = ('', 50000)
	for char in string.ascii_lowercase:
		stripped_polymer = polymer.replace(char, '').replace(char.upper(), '')
		test_polymer = polymerize(stripped_polymer)
		l = len(test_polymer)
		if (l < lowest[1]):
			lowest = (char, l)
			
	print('5.2:  lowest = {} @ {}'.format(lowest[0], lowest[1]))


# ~~~~~~~~~~~~~~~~~

if __name__ == "__main__": 
	main()