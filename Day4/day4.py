
import re

winningCards = []
holdingCards = []
newList = []
scoreSumTask1 = 0
scoreSumTask2 = 0
scoreDictTask1 = {0:0, 1:1, 2:2, 3:4, 4:8, 5:16, 6:32, 7:64, 8:128, 9:256, 10:512 }
howManyCards = {}
numCardsOverall = 0
arr = []

lineList = [line.rstrip() for line in open('input.txt')]

numCardsOverall = len(lineList)
for i in range(numCardsOverall):
	howManyCards[i+1] = 1


# Parsing input
for line in lineList:
	newList = []
	scoreTask1 = 0
	data = line.replace('|', ':')
	data = data.split(':')


# Task 1
	for idx, item in enumerate(data):

		if idx==0:
			item = item.replace('Card ', '')
			actualCard = int(item)
		if idx==1:
			winningCards = [x for x in item.split() if x.isdigit()]
		if idx==2:
			holdingCards = [x for x in item.split() if x.isdigit()]

		# Task 1 
		newList.append(item.strip())
		matchedCards = set(winningCards).intersection(holdingCards)
		numFoundedCards = len(matchedCards)
		scoreTask1 = scoreDictTask1[len(matchedCards)]
		if idx==2:
			arr.append(numFoundedCards)

	scoreSumTask1 += scoreTask1
print(f'score result Task 1: {scoreSumTask1}')


# Task 2
for idx, val in enumerate(arr):
	actualCard = idx+1
	actualCardCopies = arr[idx]

	for i in range(arr[idx]):
		temp = howManyCards[i+1+actualCard]
		howManyCards[i+1+actualCard] = temp + howManyCards[actualCard]

sumList = [howManyCards[x] for x in howManyCards]
print(f'score result Task 2: {sum(sumList)}')















		
		

