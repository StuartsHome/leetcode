# 12/09/20
# Function to do with time - there should be a leetcode question for this
	#  Times int by 60 for seconds and, work out hours and mins by dividing by 3600 ??




# Classes vs Functions - Reed Reddit post saved in Favourites.
# Linked Lists - quora explantion, search Quora browsing History
# How to leverage Stocks - take out a loan? use a stock broker? loan of 50%?
# Create stock API using Excel for real-time updates in a Excel graph
# Create a Python bot (using telegram?) that can scrape websites e.g.(Supreme for sniping latest products)




# Topics to reinforce
# Binary Trees - Preorder, Post - In order
# Depth First - Bread First Searches
# Balanced Parenthesis

# Ternary conditional operator
# in JAVA, shorter conditional operator using question mark and colon.


######################################
####### Split String into Chars
####### 
######################################


# There are two ways to split a String into chars
print(list("Hello"))
# or
s = "Hello"
x = [char for char in s]
print(x)
# for loop adds complexity
# list funtion uses additional libraries


#### To DO
	# Zip function
	# Quick Sort

	# Binary search iterative an recursive

	# STacks JAVA
	
	#CRUD apps = SQL commands: CREATE, READ, UPDATE, DELETE
	#Plot graph like GeoHot

	# java constructors
	# Java version - I use? 14?


	# Things to do

	# Work out hidden boilerpate code in leetcode
	# Python - how 1 object uses methods from 2 different classes
	# python - work with classes (self parameter)
	# traverse a tree
		# try with preorder & inorder
	# finish leetcode Chapter on Binary Trees, then move onto Recursion
	# Reddit - Understand example of Classes vs Functions(methods)

	#########
	# Quick Sort #
	#########

#Sorting algorithm, where pick 1 random number as pivot
#	put all numbers greater or larger to one end


######## random number generator
# zip tuples
#mvc



# To do 
	# Binary Search Trees 
		# Inorder - Preorder - PostOrder



#########
class Solution:
	def lcp(self, strs):
		prefix = strs[0]


		for i in range(len(strs)):
			while strs[i].find(prefix) != 0:
				a = len(prefix) - 1
				prefix = prefix[:a]

		return prefix

aa = ["Flower", "Flow", "Flock"]
p1 = Solution()
p1.lcp(aa)



#########
class Solution:
	def maxProfit(self, nums):
		counter = 0
		valley = nums[counter]
		peak = nums[counter]
		profit = 0
		while counter < len(nums) -1:
			while counter < len(nums)-1 and nums[counter] >= nums[counter + 1]:
				counter += 1
			valley = nums[counter]
			while counter < len(nums)-1 and nums[counter] <= nums[counter+1]:
				counter +=1
			peak = nums[counter]
			profit += (peak - valley)
		return profit

p1 = Solution()
p1.maxProfit([7,1,5,3,6,4])








# Algorithm Practice
# 1. BubbleSort
# 2. BinarySearch
# 3. Palindrome
# 4. Fibonacci
# 5. Roman To Int
# 6. Permute
# 7. Stocks Max Profit
# 8. Longest Common Prefix
# 9. CountAndSay??
# 10. Distributed Candies to People - (cool maths)				- Leetcode 1103
# 11. is_prime
# 12. is_valid - Balanced parenthesis (leetcode 20)
# 13. Generate Parenthesis - Backtracking approach for cool permutation recursion function
# 14. Remove Duplicates - 26. Two Pointers
# 15. Find Second Smallest Number			- Code found in this file									- StackOverflow


# Common Interview Questions
# 1. Balance Binary Tree					- using the 2 function method
# 2. Given BST, return a balanced BST																	- Leetcode 1382
# 2. Create Insert Method for BST
# 3. Reverse Linked List
# 4. preorder / inorder Tree Traversal		- Iterative and Recursive 
# 5. BST Tree Traversal
# 6. Topological Sort
# 7. Two Pointers																						- Leetcode 26
# 8. Balance Parenthesis					- 2 Methods: input int generate string, input string return True/False
# 9. Longest common prefix - Flow, Flower etc.
# 10. Product of Array Except self.			- Great Math technique - Using two pointers					- Leetcode 238
# 11. Surrounded Regions
# 12. Verifying Alien Dictionary			- Leetcode 953 - Own File
# 13. First Bad Version						- Binary Search Alternative using APi -						- Leetcode 278
# 14. TwoSum								- Adding 2 unique elements in array							- Leetcode 1
# 15. TopK Frequent Elements				- QuickSelect, or using HeapQ								- Leetcode 347
# 15. Insertion Sort
# 16. Add Binary							- Add two binary numbers									- Leetcode 67
# 17. Sum of All Left Leaves				- Traverse BT and sum leaves								- Leetcode 4047
# 18. Middle of the Linked List				- Manipulate LL into List / Fast and Slow Pointers			- Leetcode 876
# 19. House Robber							- Sliding Window, # Fast, Lagging Sliding Window Method		- Leetcode 198
# 20. Insertion Sort Linked List			- Handle multiple pointer changes and assignments			- Leetcode 147
# 21. Merge Sorted Array					- Merge 2 Sorted Arrays										- Leetcode 88
# 22. Reverse Linked List II				- M to N  Linked List Multiple Pointers						- Leetcode 92
# 23. Middle of the Linked List				- Two pointer approach										- Leetcode 876
# 24. Remove Element						- Two pointer - Similar to 26 Remove Duplicates				- Leetcode 27

# Leetcode Completed at Work
# 1331 - Rank transform of an array
# 387 - First Unique Character in a String 
# 540 - Single element in a sorted array
# 344 - Reverse String

# w/c 16th
# 1162 -	As Far from Land as Possible
# 67 -		Add Binary
# 404 -		Sum of all left leaves
# 237 -		Delete Node in a Linked List
# 876 -		Middle of the Linked List
# w/c 25th
# 92 -		Reverse Linked List II - M to N
# w/c 7/12
# -			Middle of the Linked List again!!




def romanToInt(strs):


	memo = {
		"I" : 1,
		"V" : 5,
		"X" : 10,
		"L" : 50,
		"C" : 100,
		"D" : 500,
		"M" : 1000
		}

	val =0
	for i in range(len(strs)-1):
		if memo[strs[i]] < memo[strs[i+1]]:
			val -= memo[strs[i]]
		elif memo[strs[i]] > memo[strs[i+1]]:
			val += memo[strs[i]]
		
	val += memo[strs[-1]]
	return val


romanToInt("IVVII")		


def romanToInt(n):
	
	value = 0
	for i in range(0, len(n) - 1):
		if memo[n[i]] < memo[n[i+1]]:
			 value -= memo[n[i]]
		else:
			value += memo[n[i]]
	value += memo[n[-1]]
	return value















class Solution:
	def lcp(self, strs):
		if len(strs) <= 1:
			return ""

		prefix = strs[0]
		for i in range(len(strs)):
			while strs[i].find(prefix) != 0:
				a = len(prefix) -1
				prefix = prefix[:a]
		return prefix


p1 = Solution()
p1.lcp(["Flower", "Flow", "Flowler"])




#########
# Play

######## 

list("rat")




# To Do:
	# Quick Select / Quick Sort
		# Merge Sort, Heap Sort
	# Hash Map
	# Balance BST
	# Balance Parenthesis
	# DFS and BFS in leetcode
	# Priorigty Queue is a heap implemetation





#######
4 % 4

# Test DisCandies
give = 0
candies = 4
while candies > 0:
	print(candies, give)
	print(min(candies, give +1))
	give += 1
	candies -= give

class Solution:
	def distributedCandies(self, candies, num_people):
		people = num_people * [0]
		give = 0
		while candies > 0:
			print("people, before: ", people)
			print("give:", give, "numpeople:", num_people)
			people[give % num_people] += min(candies, give+1)
			give += 1
			candies -= give
		return people



p1 = Solution()
p1.distributedCandies(7, 4)


#####

class Solution:
	def lemonadeChallenge(self, bills):
		cash = 0
		i = 0
		while i < len(bills):
			if bills[i] > 5:
				cash -= bills[i]-5
				print(cash)
				if cash < 0:
					return False
			else:
				cash +=  (bills[i])
			i+= 1
		return True
p1 = Solution()
p1.lemonadeChallenge([5,5,5,10,20])














class Solution:
	def quickSort(self, nums):
		lower = []
		equal = []
		upper = []

		if nums > 1:
			pivot = 0
			for i in nums:
				if i < pivot:
					lower.append(i)
				elif i == pivot:
					equal.append(i)
				elif i > pivot:
					upper.append(i) 
			return self.quickSort(lower) + equal + self.quickSort(upper)
		else:
			return nums

p1 = Solution()
p1.quickSort([5,10,29,45,33,13,1,3,10])





class Solution:
	def quickSort(self, nums):

		lower = []
		equal = []
		upper = []
		if nums > 1:
			pivot = nums[0]
			for x in nums:
				if x < pivot:
					lower.append(x)
				elif x == pivot:
					equal.append(x)
				elif x > pivot:
					upper.append(x)
			# don't forget to return something
			return self.quickSort(lower) + equal + self.quickSort(upper)
		else: # You need to handle the part at the end of the recursion - when you only have one element
				# in the array, just return the array
			print("#############", nums)
			return nums

p1 = Solution()
p1.quickSort([5,3,99,44,89,0,102])


class Solution:
	def maxProfit(self, nums):
		valley = 0
		peak = 0
		max_profit = 0
		i = 0
		while i < len(nums) - 1:
			while i < len(nums) - 1 and nums[i] > nums[i+1]:
				i += 1
			valley = nums[i]
			while i < len(nums) - 1 and nums[i] < nums[i+1]:
				i+=1
			peak = nums[i]
			max_profit += peak - valley
		return  max_profit

p1 = Solution()
p1.maxProfit([7, 1, 5, 3, 6, 4])



import math
class Solution:
	def is_prime(self, nums):
		if nums % 2 == 0 and nums > 2:
			return True
		for i in range(3,int(math.sqrt(nums)) + 1, 2):
			if nums % i == 0:
				return True
		return False


p1 = Solution()
p1.is_prime(7)


##################

import math
class Solution:
	def isPrime(self, num):
		if num > 2 and num % 2 == 0:
			return False
		
		for i in range(3, int(math.sqrt(num)) +1, 2):
			if i % num == 0:
				return True
		return False

p1 = Solution()
p1.isPrime(7)

##########
# When I have time, debug this code to find how it works
##########
class Solution:
	def disCandies(self, candies, num_people):
		people = num_people * [0]
		give = 0
		while candies > 0:
			people[give % num_people] += min(candies, give + 1)
			give += 1
			candies -= give
		return people


p1 = Solution()
p1.disCandies(7, 4)

##########





#########################

# Topological sort from GeeksforGeeks
# Not using a dictionary but creating one using "defaltdict"
from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list)		# dictionary containing adjacency matrix
		self.V = vertices							# No. of vertices

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)
	
	# Recursive function used by Topological Sort
	def topologicalSortUtil(self, v, visited, stack):
		# Mark the current node as visited
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)
		# Push current vertex to stack which stores result
		stack.append(v)

	# The function to do Topological Sort. It uses recursive topologicalSortUtil()
	def topologicalSort(self):
		# Mark all the vertices as not visited
		visited = [False]*self.V
		stack = []

		# Call the recursive helper function to store Topological
		# Sort starting from all vertices one by one
		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)
		# Print contents of the stack
		print(stack[::-1]) # return list in reverse order

# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

# Function Call
g.topologicalSort()
#################
#################

class Solution:
	def balanceParen(self, str):
		stack = []
		memo = {
			")" : "(",
			"}" : "{",
			"]" : "["
		}
		for i in str:
			if i in memo:
				val = stack.pop() if stack else "#"

				if val != memo[i]:
					return False
			else:
				stack.append(i)
		return not stack
			

p1 = Solution()
p1.balanceParen("(())(")



memo = {}
class Solution:
	def fibonacci(self, nums):
		if nums in memo:
			return memo[nums]
		if nums <= 2:
			return 1

		else:
			f = self.fibonacci(nums-1) + self.fibonacci(nums-2)
		memo[nums] = f

		return f
		


Run = Solution()
Run.fibonacci(10)

###############
# Second Smallest from Array
# Code taken from StackOverflow
###############


def second_largest(nums):
	count = 0
	m1 = m2 = float('-inf')					# You can use zero if numbers in array greater than 0
	for x in nums:						
		count += 1							# Using count to make sure length greater than or equal to 2
		if x > m2:
			if x >= m1:
				m1, m2 = x, m1
			else:
				m2 = x
	return m2 if count >= 2 else None


second_largest([20,67,3,2.6,7,74,2.8,90.8,85,52.8,4,3,2,10,7])



#####################
# Second largest test
#####################

class Solution:
	def second_largest(self, nums):
		count = 0
		m1 = m2 = float("-inf")

		for i in range(len(nums)):
			count += 1
			if nums[i] >= m2:
				if nums[i] >= m1:
					m1, m2 = nums[i], m1
				else:
					m2 = nums[i]
		return m1, m2 if count >= 2 else None

					



Run = Solution()
Run.second_largest([20,67,3,2.6,7,74,2.8,90.8,85,52.8,4,3,2,10,7])

# Negative infinity - Makes sure that negative infinity won't be returned when the actual answer is undefined

###############################
###############################
# Surrounded Regions

# Recursive DFS Solution to surrounded islands
# Solution we only need to do DFS on border cells.
# DFS 

grid = [
	["X", "X", "X", "X"],
	["X", "O", "O", "X"],
	["X", "X", "O", "X"],
	["X", "O", "X", "X"]
	]

class Solution:
	def solve(self, board):
		rows, cols = len(board), len(board[0])


		def dfsBorder(r,c):
			if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
				board[r][c] = "."
				dfsBorder(r + 1, c)
				dfsBorder(r - 1, c)
				dfsBorder(r, c + 1)
				dfsBorder(r, c - 1)


		for r in range(rows):
			for c in [0, cols - 1]:
				if board[r][c] == "O":
					dfsBorder(r,c)
		for c in range(1, cols -1):
			for r in [0, rows -1]:
				if board[r][c] == "O":
					dfsBorder(r,c)
		for r in range(rows):
			for c in range(cols):
				if board[r][c] == ".":
					board[r][c] = "O"
				elif board[r][c] == "O":
					board[r][c] = "X"
		return board

Run = Solution()
Run.solve(grid)



# Add binary - 67
# Solution from Leetcode Discussions

# To Solve: use columnar addition.
	# Start from the last column and add two digis and also not to forget about carry.
	# we stop when we reached beginning of both numbers

class Solution:
	def addBinary(self, a, b):
		carry = 0
		result = ""

		a = list(a)
		b = list(b)

		while a or b or carry:
			if a:
				carry += int(a.pop())		# pop to take last digits from list
			if b:
				carry += int(b.pop())
			result += str(carry % 2)		# take the remainder from the two digits
			carry = carry // 2
		return result[::-1]					# reverse the String


Run = Solution()
Run.addBinary("11", "1")


1 // 2


a = "111"
a = list(a)
print(a)

# Leetcode 404 - Sum of Left Leaves
# Code reused from Binary Tree Sum 112

# Solution from leetcode Discussions
# root is current node, 
# and side is -1 if this node is left child and +1 if this is right child.
# If we reach None node, we just return.
# If current node doesn't have children, then we check that it is left child
# of some other node, if that's correct, we add its value to global self.sum
# Finally, run recursively dfs for left children with -1  and 1 for right.



class TreeNode:
	def __init__(self, val =0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right
class Solution:
	def dfs(self, root, side):
		if root is None:
			return 
		if root.left is None and root.right is None:
			if side == -1: self.memo += root.val
		self.dfs(root.left, -1)
		self.dfs(root.right, 1)
	def SumofLeftLeaves(self, root):
		
		self.memo = 0
		self.dfs(root, 0)
		return self.memo

p4 = TreeNode(7)
p3 = TreeNode(15)
p2 = TreeNode(20, p3, p4)
p1 = TreeNode(9)
Tree = TreeNode(3, p1, p2)
Run = Solution()
Run.SumofLeftLeaves(Tree)