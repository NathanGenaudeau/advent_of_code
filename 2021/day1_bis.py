import sys

depths = open(sys.argv[1]).readlines()

count = 0
for i in range(len(depths)):
	if (i > 2 and depths[i] != '' and (int(depths[i]) + int(depths[i-1]) + int(depths[i-2])) > (int(depths[i-1]) + int(depths[i-2]) + int(depths[i-3]))):
		count += 1
print(count)