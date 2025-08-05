import sys

lines = open(sys.argv[1]).readlines()

total_square_feet = 0
for line in lines:
	[l, w, h] = [int(x) for x in line.split('x')]

	size = 2*l*w + 2*w*h + 2*h*l
	mini = min([l*w, w*h, h*l])
	total_square_feet += size + mini

print(total_square_feet)