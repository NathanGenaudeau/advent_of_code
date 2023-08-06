import sys

instructions = open(sys.argv[1]).readlines()

depth = 0
horizontal = 0
aim = 0
for instruction in instructions:
	tab = instruction.split(' ')
	if (tab[0] == 'forward'):
		horizontal += int(tab[1])
		depth += int(tab[1])*aim
	elif (tab[0] == 'up'):
		aim -= int(tab[1])
	elif (tab[0] == 'down'):
		aim += int(tab[1])
print(depth * horizontal)