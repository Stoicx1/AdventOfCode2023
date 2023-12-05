
# Task 1 - Check single arounding position 
def CheckPos(posX, posY, OffsX, OffsY, matrix):
	if matrix[posX+OffsX][posY+OffsY].isdigit() or matrix[posX+OffsX][posY+OffsY] == '.':
		return(True)
	else:
		return(False)

# Task 1 - Validation of position
def CharPosValidation(posY, posX, matrix):
	res = []
	res.append(CheckPos(posX, posY,-1,  0, matrix))
	res.append(CheckPos(posX, posY,+1,  0, matrix))
	res.append(CheckPos(posX, posY, 0, -1, matrix))
	res.append(CheckPos(posX, posY, 0, +1, matrix))
	res.append(CheckPos(posX, posY,-1, -1, matrix))
	res.append(CheckPos(posX, posY,+1, -1, matrix))
	res.append(CheckPos(posX, posY,+1, +1, matrix))
	res.append(CheckPos(posX, posY,-1, +1, matrix))
	if False in res:
		return False
	else:
		return True

# Task 2 - Check single arounding position 
def CheckMul(posX, posY, OffsX, OffsY, matrix):
	res = {}
	if matrix[posX+OffsX][posY+OffsY] == '*':
		res['y'] = posX+OffsX
		res['x'] = posY+OffsY
		return res

# Task 2
def FindGearSign(posY, posX, matrix):
	res = []
	resres = []
	res.append(CheckMul(posX, posY,-1,  0, matrix))
	res.append(CheckMul(posX, posY,+1,  0, matrix))
	res.append(CheckMul(posX, posY, 0, -1, matrix))
	res.append(CheckMul(posX, posY, 0, +1, matrix))
	res.append(CheckMul(posX, posY,-1, -1, matrix))
	res.append(CheckMul(posX, posY,+1, -1, matrix))
	res.append(CheckMul(posX, posY,+1, +1, matrix))
	res.append(CheckMul(posX, posY,-1, +1, matrix))
	for val in res:
		if val != None:
			resres.append(val)
	return resres
		




with open('test1.txt') as file:
	lines = file.readlines()
	lenLines = len(lines)
	lenline  = len(lines[0])
	digitLines = ['' for i in range(lenLines)]

# input data remove '\n'
for idx, line in enumerate(lines):
	if line.find('\n'):
		line = line[:-1]

# input data add first and last empty row
feLine = ''
for i in range(lenline-1):
	feLine += '.'
lines.insert(0, feLine)
lines.append(feLine)

# input data add first and last empty char in line
for idx, line in enumerate(lines):
	lines[idx] = line.replace('\n', '')
	lines[idx] = '.' + lines[idx] + '.'

# Traverse of matrix and find all nums
foundNum = ''
validNumsList = {}
validNumsArrFalse = []
validNumsArrTrue = []
resNum = []
mulResArr = []
mulResList = {}
for y, line in enumerate(lines):
	for x, char in enumerate(line):
		if char.isdigit():
			foundNum += char
			#print(f'testing, {x} {y} {char}')
			resNum.append(CharPosValidation(x, y, lines))
			mulResArr.append(FindGearSign(x,y,lines)) 
		elif not char.isdigit() and foundNum != '':
			#print(resNum)
			if False in resNum:
				validNumsArrFalse.append(foundNum)	
			else:
				validNumsArrTrue.append(foundNum)

			mulResList[foundNum] = mulResArr
			
			foundNum = ''
			resNum = []
			mulResArr = []
			


for line in lines:
	print(line)
print()

#print()
#print(validNumsList)
#print(validNumsArrFalse)
#print(validNumsArrTrue)
#print()

summ = 0
for val in validNumsArrFalse:
	summ += int(val)

#print(summ)
#print()

newList = {}
newtuple = ()
for val in mulResList:
	for item in mulResList[val]:
		if item:
			newList[val] = item[0]

data = newList



# Create a dictionary to store items with the same values
values = {}
tempTuple = ()
tempArr = []



for key, coordinates in data.items():
	(x, y) = coordinates['x'], coordinates['y']
	tempTuple = (x, y)
	print(tempTuple)

	'''
	try:
		tempArr = values[tempTuple]
		tempArr.append(key)
	except:
		values[tempTuple] = [key]
	'''
for val in values.items():
	key, coord = val
	#print(val)


mul = 1
muls = []
sumTot = 0
'''
# Print the result
for coordinates, keys in same_values.items():
    #print(f"Values {coordinates} have keys: {keys}")
    #print(keys)
    mul = 1 
    for key in keys:
    	mul = mul * int(key)
    muls.append(mul)
'''
#print(muls)

for val in muls:
	sumTot = sumTot + val

#print(sumTot)
#87449461














		
		

