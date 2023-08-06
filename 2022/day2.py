import sys

attempts = open(sys.argv[1]).readlines()
attempts = [x[:-1] for x in attempts]

score = 0
for attempt in attempts:
	rps = attempt.split(' ')
	if rps[0] == 'A':
		if rps[1] == 'X':
			score += 4
		elif rps[1] == 'Y':
			score += 8
		elif rps[1] == 'Z':
			score += 3
	elif rps[0] == 'B':
		if rps[1] == 'X':
			score += 1
		elif rps[1] == 'Y':
			score += 5
		elif rps[1] == 'Z':
			score += 9
	elif rps[0] == 'C':
		if rps[1] == 'X':
			score += 7
		elif rps[1] == 'Y':
			score += 2
		elif rps[1] == 'Z':
			score += 6
print(score)