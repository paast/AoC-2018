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

	block = {char: 0 for char in string.ascii_lowercase}

	for index, monomer in enumerate(polymer):
		if (skip):
			skip = False
			continue

		if (is_pair(passed[-1:], monomer)):
			passed = passed[:-1]
			block[monomer.lower()] -= 1
		elif (is_pair(monomer, polymer[index + 1])):
			skip = True
		else:
			passed += monomer
			block[monomer.lower()] += 1

	max_block = reduce(lambda a, b: a if a[1] > b[1] else b, block.items())
	return (passed, max_block)

def main():

	# load dataset
	with open("polymer.txt") as file:
		polymer = file.read()

	# 5.1
	new_polymer, max_block = polymerize(polymer)

	print(len(polymer), len(new_polymer))
	print(max_block)

	# 5.2
	remove_char = max_block[0]
	stripped_polymer = polymer.replace(remove_char.lower(), '').replace(remove_char.upper(), '')
	new_polymer, max_block = polymerize(stripped_polymer)

	print(len(stripped_polymer), len(new_polymer))
	print(max_block)


# ~~~~~~~~~~~~~~~~~

if __name__ == "__main__": 
	main()