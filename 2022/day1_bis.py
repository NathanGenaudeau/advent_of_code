import sys

elfs = open(sys.argv[1]).readlines()

top_three = [0, 0, 0]
cur = 0
for elf in elfs:
	if elf == '\n':
		for i in range(len(top_three)):
			if cur > top_three[i]:
				top_three[i] = cur
				break
		top_three.sort()
		cur = 0
	else:
		cur += int(elf)
print(sum(top_three))