from collections import namedtuple
import re

# ~~~~~~~~~~~~~~~~~

Rect = namedtuple('Rect', ['id', 'x', 'y', 'w', 'h'])

def parse_line(line):

	regex = re.compile(r'#(\d+)\ @\ (\d+),(\d+):\ (\d+)x(\d+)')

	id, x, y, w, h = map(lambda x: int(x), regex.match(line).groups())
	return Rect(id, x, y, w, h)

# auxiliary function used to find map size (1000 by 998 in this case)
def find_size(rect_list):
	max_x = 0
	max_y = 0
	for rect in rect_list:
		far_x = rect.x + rect.w
		far_y = rect.y + rect.h
		if far_x > max_x: max_x = far_x
		if far_y > max_y: max_y = far_y
	return (max_x, max_y)

def main():
	
	# load dataset
	with open('3.txt') as file:
		rect_list = [parse_line(line) for line in file.readlines()]

	# day 3.1
	map_width, map_height = find_size(rect_list)
	map = [[0] * map_width for _ in range(map_height)]

	for rect in rect_list:
		for y in range(rect.h):
			y = rect.y + y
			for x in range(rect.w):
				x = rect.x + x
				map[y][x] += 1

	count = sum([len(list(filter(lambda x: x > 1, l))) for l in map])
	print('3.1:  overlap (in^2): {}'.format(count))

	# day 3.2
	for rect in rect_list:
		the_one = True
		for y in range(rect.h):
			y = rect.y + y
			for x in range(rect.w):
				x = rect.x + x
				if (map[y][x] != 1):
					the_one = False
		if (the_one): print('3.2:  id: {}'.format(rect.id))


# ~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
	main()

# concept:
#	> parse each line into a Rect
# 	> find map size
#	> create 2-D array with map size
#	> fill in rects on map
#	> find sum of > 1 squares (3.1)
#	> same thing as fill, but print any rect that never overlaps (3.2)