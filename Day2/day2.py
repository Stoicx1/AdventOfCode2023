




def parseData():
	print('parse data')


# -----------------------------------------------
# task 1
# -----------------------------------------------

maxRed   = 12
maxGreen = 13
maxBlue  = 14

with open('input.txt') as file:
	lines = file.readlines()
	lenLines = len(lines)
	digitLines = ['' for i in range(lenLines)]

summTask1 = 0
summTask2 = 0
for idx, game_str in enumerate(lines):
	biggestRed   = 0
	biggestGreen = 0
	biggestBlue  = 0

	events_part = game_str.split(': ')[1]

	linePossible = True
	parsed = []
	for val in events_part.split(';'):
		event = {}
		for item in val.split(','):
			quantity, color = item.strip().split()
			event[color] = int(quantity)

			# Task 1 - logic
			if color == 'red' and int(quantity) > maxRed:
				linePossible = False
			if color == 'green' and int(quantity) > maxGreen:
				linePossible = False
			if color == 'blue' and int(quantity) > maxBlue:
				linePossible = False

			# Task 2 - logic
			if color == 'red':
				if biggestRed < int(quantity):
					biggestRed = int(quantity)
			if color == 'green':
				if biggestGreen < int(quantity):
					biggestGreen = int(quantity)
			if color == 'blue':
				if biggestBlue < int(quantity):
					biggestBlue = int(quantity)

	# Task 1 sum
	if linePossible:
		summTask1 = summTask1 + (idx+1)

	# Task 2 sum
	mul = biggestRed * biggestGreen * biggestBlue
	summTask2 += mul

print()
print(summTask1)
print(summTask2)



# -----------------------------------------------
# task 2
# -----------------------------------------------

	
	



		
		

