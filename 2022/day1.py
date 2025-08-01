import sys

elfs = open(sys.argv[1]).readlines()

maxi = 0
cur = 0
for elf in elfs:
	if elf == '\n':
		maxi = cur if cur > maxi else maxi
		cur = 0
	else:
		cur += int(elf)
print(maxi)