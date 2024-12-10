# P1: Q: What is the sum of all of the calibration values?

# Read through file

file = open('input.txt')
lines = file.readlines()

# Loop through the list returned and get the first number and the last number on the line

def findNums(lines): # Define function
    numList = [] # Declare and initialise a new list
    for line in lines: # Retrieve line in this index
        firstNum = None # Declare and initialise var to null
        lastNum = None # Declare and initialise var to null
        for char in line: # For each char in this string
            if char.isdigit(): # Check it's digit
                if firstNum is None: # Check if var has value
                    firstNum = char # Update if no value
                lastNum = char # Continuously update value until last digit in string
        if firstNum is not None and lastNum is not None: # Check bothe var have data
            fullNum = int(str(firstNum) + str(lastNum)) # Concatanate and convert to int when 1 string is complete
            numList.append(fullNum) # Append 2 digit number to list
    return numList # Return list of multiple 2 digit numbers when all lines have been looped through

# When looping is done, add the numbers together
fullSum = sum(findNums(lines))
print(fullSum)

# First attempt number: 543161
# Second attempt number: 25021
# Third attempt number: 52380
# Last attempt: Right answer!