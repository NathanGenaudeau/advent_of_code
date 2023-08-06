import sys

lines = open(sys.argv[1]).readlines()

total_square_feet = 0
for line in lines:
	[l, w, h] = [int(x) for x in line.split('x')]
	sort = [l, w, h]
	sort.remove(max(sort))

	size = 2*sum(sort) + l*w*h
	total_square_feet += size

print(total_square_feet)