import re

digitLines = []
lenLines = 0

def first_and_last_digits_string(number):
    # Convert the number to a string
    num_str = str(number)

    # Concatenate the first and last digits as a string
    if len(number)>1:
    	first_digit = num_str[0]
    	last_digit = num_str[-1]
    	result = first_digit + last_digit
    elif len(number)==1:
    	first_digit = num_str[0]
    	last_digit = num_str[-1]
    	result = first_digit + first_digit
    else:
    	result = 0
    return result

def replace_words_with_digits(input_string):
    # Define a mapping for words to digits
    my_dict = {}
    res = ''
    word_to_digit_mapping = {
		'one'  : 'o1e',
		'two'  : 't2o',
		'three': 't3e',
		'four' : 'f4r',
		'five' : 'f5e',
		'six'  : 's6x',
		'seven': 'se7en',
		'eight': 'e8t',
		'nine' : 'n9ne'
	}

    for key in word_to_digit_mapping:
    	input_string = input_string.replace(key, word_to_digit_mapping[key])

    return input_string



# -----------------------------------------------
# task 1
# -----------------------------------------------
with open('input.txt') as file:
	lines = file.readlines()
	lenLines = len(lines)
	digitLines = ['' for i in range(lenLines)]

summ = 0
for idx, line in enumerate(lines):
	temp = ''
	l = line.rstrip()

	for char in line:
		if char.isdigit():
			temp = temp + str(char)
	digitLines[idx] = temp

	value = first_and_last_digits_string(temp)
	summ = summ + int(value)
print('Result task 1:',summ)

# -----------------------------------------------
# task 2
# -----------------------------------------------
with open('input.txt') as file:
	lines = file.readlines()
	#lines = ['oneight18oneight18']
	lenLines = len(lines)
	digitLines = ['' for i in range(lenLines)]


summTask2 = 0
for idx, line in enumerate(lines):
	temp = ''
	l = line.rstrip()
	value = replace_words_with_digits(l)

	for char in value:
		if char.isdigit():
			temp = temp + str(char)

	value = first_and_last_digits_string(temp)
	summTask2 = summTask2 + int(value)
print('Result task 2:',summTask2)


	
	



		
		

