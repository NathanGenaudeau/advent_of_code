import sys

instructions = open(sys.argv[1]).readlines()

depth = 0
horizontal = 0
for instruction in instructions:
	tab = instruction.split(' ')
	if (tab[0] == 'forward'):
		horizontal += int(tab[1])
	elif (tab[0] == 'up'):
		depth -= int(tab[1])
	elif (tab[0] == 'down'):
		depth += int(tab[1])
print(depth * horizontal)