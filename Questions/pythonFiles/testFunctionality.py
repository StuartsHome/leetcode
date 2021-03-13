#### Test Functionality

# Python Style -
	# "node is not None" instead of "(node != None)"
	# "__str__" instead of own print function in a class.
	
# Converting integer to List
# Can use map for a map return type
# or List Comprehension

[int(x) for x in str(nums)]

##############################################
############################### String formatting
##############################################
# The End Statement
# The default end statement in Python is "\n"
# Changing the end statement to 'end=""' removes the newline e.g.

print("Hello", end="")
print("My name is Stuart")

# The Sep Statement
# Opposite of end

print("Hello", "My name is Stuart")
print("Hello", "My name is Stuart", sep=" ")

print("Hello", "My name is Stuart", sep = " & ")
print("Hello", "My name is Stuart", "What is your name", sep = " & ")

# The Join Statement - On Tuples and Lists

myTuple = ("Stuart", "David", "Smith")
myList = ["Stuart", "David", "Smith"]

print(" ".join(myTuple))
print(" ".join(myList))


# The Join Statement - On Strings

myTuple = ("Stuart", "David", "Smith")
myList = ["Stuart", "David", "Smith"]

print(" ".join(myTuple))
print(" ".join(myList))

text = "lorem ipsum dolla spar. seperate and is the. falling and yup. donw them"
print("@".join(text))

# The Split statement

text = "lorem ipsum dolla spar. seperate and is the. falling and yup. donw them."
print(text.split(". "))

# Thousands seperator
number = 20001010101010
print("{:,}".format(number))

# Round number to n digits
number = 2321.561010101010
print(round(number, 1))

# Format string into tidily-aligned set of columns giving integers and their squares and cubes.
for i in range(1, 11):
	print("{0:2d} {1:3d} {2:2d}".format(i, i*i, i*i*i))

########
# Range
########

# Range 5 does 5 iterations starting at 0. So 0 - 4


# Evaluation Order
# IN an assignment statement, the right-hand side is always evaluated fully before doing the actual
# setting of variables, e.g.

y = nums[i]
nums[i] = nums[pos]
nums[pos] = y

# The above is equivalent to:
nums[pos], nums[i] = nums[i], nums[pos]

# The below is from StackOverflow
x, y = y, x + y

# Like this

ham = y
spam = x + y
x = ham
y = spam


# Or

y = x + y
x = y
####################


# By contrast,
x = y
y = x + y

# Sets x to y, then sets y to x (which == y) plus y, so its equivalent to:

x = y
y = y + y


#################
# List Comprehension
#################

# For loop inside square brackets is called List Comprehension
# This should be read as: For each item in YOUR_LIST, assign the new value to NEW_VALUE
new_list = [NEW_VALUE for item in YOUR_LIST]



########
# List Method
########

# The List method can only be used on Strings 

a = "111"
a = list(a)
print(a)

########
# Using Dictionaries / Enumerate
########

s = "leetcode"
for ind, element in enumerate(s):
	print(ind, element)


########
# Build frequency Dictionary - Find the "K" frequency
########

# Use Collections - Counter
from collections import Counter
nums = [1,1,1,2,2,3,5,10,10]
memo = Counter(nums)



#########
# Alien Dictionary Design Methods
#######

# Comparing two Strings in same array
for i in range(len(words)-1):					# Range is -1 because, word2 index in +1 and will "Index out of range" if no -1.
	word1 = words[i]		
	word2 = words[i+1]			

# Looping through 2 Strings of different length at same time
for k in range(min(len(word1), len(word2))):	# Use the "min" function
	pass

# If two strings don't compare either too big, or too small
# First find if there is a difference in the array
# Then narrow down to the memo dictionary if the actual values are smaller or larger

if word1[k] != word2[k]:
	if memo[word1[k]] > memo[word2[k]]:
		pass
	#	return False
	#break


#######
## Modulo for max time
#######

total = 10 * 60 + 13	# WORKS
total // 60
total % 60
total = 10 * 60 + 123	# DON'T Work
total // 60
total % 60


##################################
# Notes:
# The modulo function for time only works when 2 digits, not 3
# E.g. 
# total = 10 * 60 + 13	WORKS
# total = 10 * 60 + 123	DON'T Work
##################################

########
# For borders in BFS / DFS search file "surrounded_Regions"
########


# 1. For each corner of the matrix use square brackets
# 2. For each cell in the border rows and columns use "range" and "in" for loops
# 3. For each first and last cell in the row use one "range" and "in" loop


# 1. ##########
for r in [0, rows-1]:
	for c in [0, cols-1]:
			board[r][c] = "Y"
print(board)

# 2. ##########
for r in range(rows):
	for c in (0, cols - 1):
		board[r][c] ="NO"
for c in range(1, cols -1):
	for r in (0, rows -1):
		board[r][c] = "YES"
print(board)

# 3. ##########
for r in range(rows):
	for c in (0, cols - 1):
		board[r][c] ="NO"
print(board)



# Two methods:
	# 1. Select borders using two For loops. One for Rows, One for Columns.
	#		select the first and final using square brackets

for r in [0, len(grid)-1]:					# 1. The first FOR statement selects the ROW "0" and final ROW in grid
	for c in range(len(grid[0])):			# For the two rows selected, Loop for how many columns in a ROW
		self.dfs(grid, r, c)

	# 2. 

########
## BFS / DFS on grids - Not touching Borders
########

if( 0 <= r < len(board) and 0 <= c < len(board[0])):
	pass

########
## If variable has no value
########

def dfs(r, c, seen = None, path=None):
	if seen is None: seen = []
	if path is None: path = [v]



#######
# Map
#######

# Executes a specified function for each item in an iterable. The item is sent to the function as a parameter

def myFunc(a, b):
	return a+b

x = map(myFunc, (1, 2, 3), (10, 20, 30))
print(list(x))


#######
# Itertools Permutations
#######
	# Takes an arbitrary iterable as an argument,
	# and always returns an iterator yeilding tuples.
# To get a list of Strings, join the tuples with:

list(map("".join, itertools.permutations("String")))

######
# Max and Min values for INTS
######

anInt = float('inf')
print(anInt)

# For smaller than 0 - use a negative
anInt = float('-inf')


# or sys - requiring a library

import sys
anInt = sys.maxsize
print(anInt)




########
### String format
########

# Signifies at least 6 characters
'{:06}'

# Signifies 6 characters
'{:6}'


# ":" signifies a format spec
"{:02d}:{:02d}".format(max_time // 60, max_time % 60)

########
## Hacker Rank - Read input from STDIN
########

# Here the variable contains the input line as string
my_string = input()

# If we then want to print the contents of whatever we saved to "my_string", we write the following:
print(my_string)

# print to STDOUT - whatever is output in the program is sent to "__main__" and stored in "my_str" then printed.
if __name__ == '__main__':
	my_str = read()
	print(my_str)


########
## Modulo
########


## Palindrome Maths
	# Cool


# to gather index of array
array1 = 4 * [0]
1 % 4
2 % 4
array1[1 % 4]




##########
## Creating empty arrays
##########

#### 1D or 2D no "For" loop
aux = 5 * [0]
print(aux)

# Note 0 * len(nums) doesnt return an array
L = [0] * len(nums)


aux = [x for x in range(4)]
print(aux)

### 1D Array
aux = [0 for x in range(4)]
print(aux)


### 2D Array
aux = [[1 for x in range(10)] for x in range(10)]
print(aux)







# Python max function
	# takes two parameters, returns the item with the highest value.
	# in this example, we're comparing the old "max_value" with the new value
	# The "hour" is * 60 because there are 23 hours of 60 minutes each.
# The ".format" method formats the specified value(s) and insert them inside the string;s placeholder
	# the placeholder is defined by using curly brackets

txt1 = "My name is {fname}, I am {age}".format(fname = "John", age=36)	  
txt2 = "My name is {0}, I am {1}".format("John",36)
txt3 = "My name is {}, I am {}".format("John", 36)
print(txt1, "\n", txt2, "\n", txt3)
print(max([22, 44, 55, 66]))


# Dictionaries - Adding key value pairs
memo = {'key' : 'value'}
print(memo)
memo['NewKey'] = 'NewValue'
print(memo)



#  Remove Punctuation string	
ww = "aa, ee, er, ww, eeee"
ww = ww.replace(',', '')
print(ww)


ww = "aa, ee, er, ww, eeee"
ww = ww.replace(',', '')
print(len(ww))


ww = [aa, ee, er, ww, eee]
ww = 123

print(len(ww))


####################
#### Slice List ###
####################

a = [5, 6, 7, 8, 9, 10]
print(a[1:4])

#Increment
a = [5, 6, 7, 8, 9, 10]
print(a[1:4:2])

# Slicing lists has functionality that:
	# If there is no value before the first colon - it means start at the begining index of the list
	# If there is no value after the first colon - it means go all the way to the end of the list

a = [5, 6, 7, 8, 9, 10]
print(a[::-1])

a = [5, 6, 7, 8, 9, 10]
print(a[0+1:])

# Select the first element from the list
a = [5, 6, 7, 8, 9, 10]
print(a[:1])

####################
#### Split String ##
####################

# Splits a string into a list, where each word is a list item
text = "LN1 2DW, DN21 5BJ, DN21 5B"
text1 = ["LN1", "2DW", "DN21", "5BJ", "DN21", "5B"]
print(text1)
text1.split(",")

number = len(text.split(','))
print(number)



####################
#### Len and count #
####################
list.count() # counts how many times the given value appears
sample = [2, 10, 1, 1, 5, 2]

len(sample)
sample.count(1)




#####################
# List of floats and ints, with duplicates
#####################
([20,67,3,2.6,7,74,2.8,90.8,85,52.8,4,3,2,10,7])




#################
## Inbounds of GRID
#################



class Solution:
	def twoSum(self, nums, target):
		
		memo = {}
		results = []
		for i in range(len(nums)):
			lookup = target - nums[i]
			if lookup in memo:
				results.append([i, nums.index(lookup)])
			memo[nums[i]] = nums[i]
		return results

Run = Solution()
Run.twoSum([1,5,7,9], 6)