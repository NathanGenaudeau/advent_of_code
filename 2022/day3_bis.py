import sys

items = open(sys.argv[1]).readlines()
items = [x[:-1] for x in items]

total = 0
for i in range(0, len(items), 3):
	if items[i] != '' :
		commonItem = list(set(items[i]).intersection(set(items[i+1])).intersection(set(items[i+2])))[0]
		number = ord(commonItem) - 38 if commonItem.isupper() else ord(commonItem) - 96
		total += number
print(total)