import sys

lines = open(sys.argv[1]).readlines()

def isWinner(card):
  values = list(card.values())
  if (values[0] and values[1] and values[2] and values[3] and values[4] or
      values[5] and values[6] and values[7] and values[8] and values[9] or
      values[10] and values[11] and values[12] and values[13] and values[14] or
      values[15] and values[16] and values[17] and values[18] and values[19] or
      values[20] and values[21] and values[22] and values[23] and values[24] or
      values[0] and values[5] and values[10] and values[15] and values[20] or
      values[1] and values[6] and values[11] and values[16] and values[21] or
      values[2] and values[7] and values[12] and values[17] and values[22] or
      values[3] and values[8] and values[13] and values[18] and values[23] or
      values[4] and values[9] and values[14] and values[19] and values[24]):
    return True
  return False

numbers = lines[0].split(',')
lines.pop(0)

bingoCards = []
bingoCard = {}

for line in lines:
  line = line.replace('\n', '')
  if (line == '' and len(bingoCard) > 0):
    bingoCards.append(bingoCard)
    bingoCard = {}
  else:
    nb = line.split(' ')
    for i in nb:
      if i != '': bingoCard[int(i)] = False

i = 0

while (len(bingoCards) >= 1 and i < len(numbers) and not isWinner(bingoCards[0])):
  j = 0
  while j < len(bingoCards):
    if (int(numbers[i]) in bingoCards[j].keys()):
      bingoCards[j][int(numbers[i])] = True
    if (isWinner(bingoCards[j]) and len(bingoCards) > 1):
      bingoCards.pop(j)
    else: 
      j += 1
  i += 1

sumCard = sum(i for i, j in bingoCards[0].items() if j == False)
print(sumCard * int(numbers[i-1]))
