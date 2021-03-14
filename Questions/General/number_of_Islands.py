##########
# Leetcode Number of Islands
##########

# The BFS code will run until the queue is empty, meaning there is no more land positions to visit


grid = [
	["1","1","1","1","0"],
	["1","1","0","1","0"],
	["1","1","1","0","0",],
	["0","0","0","0","0",]
]
import collections
class Solution:
	def numIslands(self, grid):
		if not grid:		# if empty grid don't run algorithm and return 0
			return 0		

		rows, cols = len(grid), len(grid[0])	# get the dimensions of the grid
		visited = set()							# could use a 2D grid instead
		islands = 0
		q = collections.deque()					# queue is normally used for memory in BFS
		def bfs(r, c):										# BFS is iterative - so needs memory source
									
			visited.add((r,c))								# mark this cell visited by adding to visited - Should be a tuple as a pair not two elements seperately
			q.append((r,c))									# also mark visited by adding to queue

			while q:											# while the queue is not empty, we're going to be expanding our island
				print(q)
				row, col = q.popleft()							# pop from the queue
				print("New", q, row, col)
				directions = [[1,0], [-1,0], [0,1], [0,-1]]		# now check the adjacent positions of the cell we just popped. Use a loop for the 4 directions we can move.
																# directions - RIGHT, LEFT, ABOVE, BELOW
				for dr, dc in directions:						# For each of these directions - X and Y of same direction co-ordinates
					if ((row + dr) in range(rows) and				# We check that each position is inbounds - First the 
						(col + dc) in range(cols) and					# Then the column + the direction we're moving in is also in range of columns
						grid[row + dr][col + dc] == "1" and				# Then that this position is a Land position
						(row + dr, col + dc) not in visited):				# Lastly, that this position hasn't already been visited
						q.append((row + dr, col + dc))					# If this is true then we can add this cell to the queue meaning we have to perform BFS on it.
						visited.add((row + dr, col + dc))				# We also have to mark it visited, so we don't visit it twice.

		for r in range(rows):									# Want to visit every position in the grid, let's iterate over each row and column.
			for c in range(cols):
				if grid[r][c] == "1" and (r,c) not in visited:	# If we visit a 0 we don't do anything
					bfs(r, c)									# run BFS on this cell
					islands += 1								# only increment the "1"'s if the cell hasn't already been visited
		return islands



p1 = Solution()
p1.numIslands(grid)


# We are doing the computation of row + direction of row a lot, so we can fix this by
	# r,c = row + dr, col + dc

"""
for dr, dc in directions:						# For each of these directions - THIS IS A INBOUNDS of GRID
					if ((r + dr) in range(rows) and				# We check that each position is inbounds - First the 
						(c + dc) in range(cols) and					# Then the column + the direction we're moving in is also in range of columns
						grid[r + dr][c + dc] == "1" and				# Then that this position is a Land position
						(r + dr, c + dc) not in visit):				# Lastly, that this position hasn't already been visited
						q.append((r + dr, c + dc))					# If this is true then we can add this cell to the queue meaning we have to perform BFS on it.
						visited.add((r + dr, c + dc))
"""

################
# Number of Islands - Depth First
################
grid = [
	["1","1","1","1","0"],
	["1","1","0","1","0"],
	["1","1","0","0","0",],
	["0","0","0","0","0",]
]
import collections
class Solution:
	def numIslands_DFS(self, grid):
		if not grid or not grid[0]:
			return 0

		islands = 0
		q = collections.deque()
		visited = set()
		rows, cols = len(grid), len(grid[0])

		def dfs(r, c):
			if (r not in range(rows) or
				c not in range(cols) or
				grid[r][c] == "0" or
				(r,c) in visited):
				return

			visited.add((r,c))
			directions = [[0,1], [0,-1],[1,0],[-1,0]]
			for dr, dc in directions:
				dfs(r + dr, c + dc)

		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == "1" and (r,c) not in visited:
					islands += 1
					dfs(r,c)
		return islands


p1 = Solution()
p1.numIslands_DFS(grid)

#################
# Alternative DFS approach - recursive - less code / more elegant
#################
grid = [
	["1","1","1","1","0"],
	["1","1","0","1","0"],
	["1","1","0","0","0",],
	["0","0","0","0","0",]
]
class Solution:
	def numIslands_DFS2(self, grid):
		if not grid or not grid[0]:
			return 0
		# iterate over the arrays
		islands = 0
		for r in range(len(grid)):
			for c in range(len(grid[0])):
				if grid[r][c] == "1":
					# increment the num counter if an island is discovered
					islands += self.dfs(r, c, grid)
		return islands

	def dfs(self, r, c, grid):
		# perform a dfs search around the 1 to check for more 1's
		if self.outofbounds(r,c,grid) or grid[r][c] is not "1":
			return 0
		grid[r][c] = "2"	# mark as visited
		self.dfs(r, c+1, grid)
		self.dfs(r, c-1, grid)
		self.dfs(r + 1, c, grid)
		self.dfs(r-1, c, grid)
		return 1
	def outofbounds(self, r, c, grid) -> bool:
		return r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])

p1 = Solution()
p1.numIslands_DFS2(grid)


# Simple BFS example from edpresso
class Solution:
	visited = []
	queue = []

	def bfs(visited, graph, node):
		visited.append(node)
		queue.append(node)

		while queue:
			s = queue.pop(0)
			print(s, end="")

			for neighbour in graph[s]:
				if neighbour not in visited:
					visited.append(neighbour)
					queue.append(neighbour)

p1 = Solution()
#p1.bfs()

######################################
######################################
# Below taken from "balance_Parentheses
######################################


####################
### Leetcode - Surrounded Regions
####################


grid = [
	["X", "X", "X", "X"],
	["X", "O", "O", "X"],
	["X", "X", "O", "X"],
	["X", "O", "X", "X"]
	]

import collections
class Solution:
	def solve(self, grid):
		rows, cols = len(grid), len(grid[0])
		queue = collections.deque()
		visited = set()
		islands = 0
		
		def bfs(r, c):
			queue.append((r,c))
			visited.add((r,c))

			while queue:
				row, col = queue.popleft()
				directions = [[0,1], [0,-1],[1, 0], [-1,0]]
				for dr, dc in directions:
					print(dr, dc) 



		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == "O" and (r,c) not in visited:
					bfs(r,c)
					islands += 1
		return islands

p1 = Solution()
p1.solve(grid)

# Leetcode Islands - BFS Examples using two different grids.
	# Not using Deque
	# queue behaves like 

grid = [
	["1","1","1","1","0"],
	["1","1","0","1","0"],
	["1","1","0","0","0",],
	["0","0","0","0","0",]
]

grid = [
	["X", "X", "X", "X"],
	["X", "O", "O", "X"],
	["X", "X", "O", "X"],
	["X", "O", "X", "X"]
	]

import collections
class Solution:
	def numIslands(self, grid):
		if not grid:		# if empty grid don't run algorithm and return 0
			return 0		

		rows, cols = len(grid), len(grid[0])	# get the dimensions of the grid
		visited = set()							# could use a 2D grid instead
		islands = 0
		q = collections.deque()					# queue is normally used for memory in BFS
		def bfs(r, c):										# BFS is iterative - so needs memory source
									
			visited.add((r,c))								# mark this cell visited by adding to visited - Should be a tuple as a pair not two elements seperately
			q.append((r,c))									# also mark visited by adding to queue

			while q:											# while the queue is not empty, we're going to be expanding our island
				print(q)
				row, col = q.popleft()							# pop from the queue
				print("New", q)
				directions = [[1,0], [-1,0], [0,1], [0,-1]]		# now check the adjacent positions of the cell we just popped. Use a loop for the 4 directions we can move.
																# directions - RIGHT, LEFT, ABOVE, BELOW
				for dr, dc in directions:						# For each of these directions - X and Y of same direction co-ordinates
					if ((row + dr) in range(rows) and				# We check that each position is inbounds - First the 
						(col + dc) in range(cols) and					# Then the column + the direction we're moving in is also in range of columns
						grid[row + dr][col + dc] == "O" and				# Then that this position is a Land position
						(row + dr, col + dc) not in visited):				# Lastly, that this position hasn't already been visited
						q.append((row + dr, col + dc))					# If this is true then we can add this cell to the queue meaning we have to perform BFS on it.
						visited.add((row + dr, col + dc))				# We also have to mark it visited, so we don't visit it twice.

		for r in range(rows):									# Want to visit every position in the grid, let's iterate over each row and column.
			for c in range(cols):
				if grid[r][c] == "O" and (r,c) not in visited:	# If we visit a 0 we don't do anything
					bfs(r, c)									# run BFS on this cell
					islands += 1								# only increment the "1"'s if the cell hasn't already been visited
		return islands



p1 = Solution()
p1.numIslands(grid)


#  DFS !!!!!!!!!!!!!

grid = [
	["1","1","1","1","0"],
	["1","1","0","1","0"],
	["1","1","0","0","0",],
	["0","0","0","0","0",]
]

class Solution:
	def num_islandsDFS(self, grid):

		#islands = 0
		visited = set()
		max_length = 0
		counter = 0
		rows, cols = len(grid), len(grid[0])

		def dfs(r,c, counter):
			if (r not in range(rows) or
				c not in range(cols) or
				grid[r][c] == "0" or
				(r,c) in visited):
				#max_length = max(counter, max_length)
				counter = 0
				return
			counter += 1
			visited.add((r,c))
			directions = [[0,1],[0,-1],[1,0],[-1,0]]
			for dr, dc in directions:
				dfs(r + dr, c + dc,counter)

		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == "1" and (r,c) not in visited:
					#islands += 1
					dfs(r,c, counter)
		#return max_length


p1 = Solution()
p1.num_islandsDFS(grid)



grid = [
	["1","1","1","1","0"],
	["1","1","0","1","0"],
	["1","1","0","0","0",],
	["0","0","0","0","0",]
]

class Solution:
	def num_islandsDFS(self, grid):

		visited = set()
		rows, cols = len(grid), len(grid[0])


		def dfs(r,c):
			if (r,c) in visited:
				return



		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == "1" and (r,c) not in visited:
					dfs(r,c)

		#return path


p1 = Solution()
p1.num_islandsDFS(grid)

# Leetcode Example - SuperDuper fast, DFS not using a stack
	# Instead of a stack, it hashes the co-ordinates of every 1 that has been visited

grid = [
	["1","1","1","1","0"],
	["1","1","0","1","0"],
	["1","1","0","0","0",],
	["0","0","0","0","0",]
]

class Solution:
	def numIslands(self, grid):
		if not grid:
			return 0
		count = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == "1":
					self.dfs(grid, i, j)
					count += 1

		return count

	def dfs(self, grid, i, j):
		if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
			return
		grid[i][j] = "#"
		self.dfs(grid, i+1, j)
		self.dfs(grid, i-1, j)
		self.dfs(grid, i, j+1)
		self.dfs(grid, i, j-1)

p1 = Solution()
p1.numIslands(grid)


# Next tidy up the example of "r,c = row + dr
	# debug the alternative DFS approach
	
	# in both, DFS and BFS switch Collections.deque to a queue without the Collections module.


# For leetcode 130 - Surrounded Regions
	# "O" on the border are not flipped to "X" 
	# How do you test if a "O" is on the border?




# As Far from Land as Possible - Leetcode 1162
# Solution Steps:
# 1. Store all land positions in a queue (deque)
# 2. Explore the sea positons (0) from land
# 3. Increase distance for each 
# 4. When position in directions visited change to land (1) to not visit again.
	# This feature replaces the need for a visited set.

# You need to start with a queue full of 1 positions from the start .
# It doesn't work when you dynamically add to the queue

grid = [
	[1,0,1],
	[0,0,0],
	[1,0,1]
	]

from collections import deque

rows, cols = len(grid), len(grid[0])

# a good way to queue all elements where to start BFS
q = deque([(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == 1]) 
print(q)

# code from leetcode discussions - 1162
# This code doesn't return the co-ordinates of the cell
# and doesn't include the formula for the Manhattan Distance
grid = [
	[1,0,1],
	[0,0,0],
	[1,0,1]
	]
from collections import deque

class Solution:
	def maxDistance2(self, grid):
			m,n = len(grid), len(grid[0])
			q = deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])    
			if len(q) == m * n or len(q) == 0: return -1
			level = 0
			while q:
				size = len(q)
				for _ in range(size):
					i,j = q.popleft()
					for x,y in [(1,0), (-1, 0), (0, 1), (0, -1)]:
						xi, yj = x+i, y+j
						if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
							q.append((xi, yj))
							grid[xi][yj] = 1
				level += 1
			return level-1 

Run = Solution()
Run.maxDistance2(grid)

# My copy of the solution from Leetcode Discussions
# Use this as the solution for 1162

grid = [
	[1,0,1],
	[0,0,0],
	[1,0,1]
	]

from collections import deque


class Solution:
	def maxDistance3(self, grid):
		rows, cols = len(grid), len(grid[0])

		# a good way to queue all elements where to start BFS
		q = deque([(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == 1]) 
		# if all cells are islands return -1
		if len(q) == rows*cols or len(q) == 0: return -1
		level = -1

		while q:
			# loop for the size of the queue (number of land cells)
			size = len(q)
			for _ in range(size):
				row, col = q.popleft()
				directions = [[0,1],[1,0],[0,-1], [-1,0]]
				for dr, dc in directions:
					if ((dr + row) in range(rows) and
						(dc + col) in range(cols) and 
						grid[dr + row][dc + col] == 0):
						q.append((dr + row, dc + col))
						grid[dr + row][dc + col] = 1
			level += 1
		return level

Run = Solution()
Run.maxDistance3(grid)





###################


# Leetcode 695
grid = [
	["0","0","1","0","0","0","1","0","0","0","0","0","0"],
	["0","0","0","0","0","0","1","1","1","0","0","0","0"],
	["0","1","1","0","1","0","0","0","0","0","0","0","0",],
	["0","1","0","1","1","0","0","0","1","0","1","0","0",],
	["0","1","0","1","1","0","0","0","1","1","1","0","0",],
	["0","0","0","0","0","0","0","0","0","0","1","0","0",],
	["0","0","0","0","0","0","0","1","1","1","0","0","0",],
	["0","0","0","0","0","0","0","1","1","0","0","0","0",]
	
]


grid = [
	["1","1","0","0","0"],
	["1","1","0","0","0"],
	["0","0","0","1","1",],
	["0","0","0","1","1",]
]


grid =[
	[0]


	]
import collections
class Solution:
	def maxAreaOfIsland(self, grid):
		if not grid:		
			return 0		

		rows, cols = len(grid), len(grid[0])	
		visited = set()							
		islands = 0
		q = collections.deque()
		counter = 1
		total = []
		def bfs(r, c, counter):							
									
			visited.add((r,c))					
			q.append((r,c))						

			while q:											
				#print(q)
				row, col = q.popleft()							
				#print("New", q, row, col)
				directions = [[1,0], [-1,0], [0,1], [0,-1]]		
																
				for dr, dc in directions:						
					if ((row + dr) in range(rows) and			
						(col + dc) in range(cols) and			
						grid[row + dr][col + dc] == "1" and		
						(row + dr, col + dc) not in visited):
						counter += 1
						q.append((row + dr, col + dc))			
						visited.add((row + dr, col + dc))
			return total.append(counter)
		for r in range(rows):									
			for c in range(cols):
				if grid[r][c] == "1" and (r,c) not in visited:	
					bfs(r, c, counter)
					#total = max(total, counter)
		return total



p1 = Solution()
p1.maxAreaOfIsland(grid)




class Solution:
	def removeElement(self, nums, val):
		i = 0
		n = len(nums)

		while i < n:
			if nums[i] == val:
				nums[i] = nums[n -1]
				n -= 1
			else:
				i += 1
		return n
Run = Solution()
Run.removeElement([3,2,2,3],3)



class Solution:
	def moveZeroes(self, nums):
		pos = 0
		for i in range(len(nums)):
			if nums[i] != 0:
				y = nums[i]
				nums[i] = nums[pos]
				nums[pos] = y

				# The above is equivalent to:
				# nums[pos], nums[i] = nums[i], nums[pos]


				pos += 1
		return nums


Run = Solution()
Run.moveZeroes([4,2,4,0,0,3,0,5,1,0])


([0,1])




([0,1,0,3,12])





([0,0,1])



class Solution:
	def lengthOfLastWord(self, s):
		if len(s) == 0:
			return 0

		text = s.split(" ")
		len_text = len(text)

		while len_text:
			if text[len_text -1 ] == "":
				len_text -= 1
			else:
				return len(text[len_text - 1])
		return 0
Run = Solution()
Run.lengthOfLastWord("a ")

("Hello World")

(" ")



# Surrounded Regions - Leetcode 130

# Leetcode Solution - From Discussions
	# If we start from "O" at the border, and we traverse only "O". 
	# The plan is the following:
		# 1. Start DFS/BFS from all "O" on the border
		# 2. When we traverse them, let us colour them "T" for temporary.
		# 3. Now, when we traverse all colors which are not "T",
		#		we change them to "X" and all colours which are "T" need to be renamed to "O".

# Original Unchanged - This method for DFS is worse than method 2!!!
grid = [
	["X", "X", "X", "X"],
	["X", "O", "O", "X"],
	["X", "X", "O", "X"],
	["X", "O", "X", "X"]
	]

import collections
class Solution:
	def solveDFS(self, grid):
		if not grid or not grid[0]:
			return
		for r in [0, len(grid)-1]:							# 1. The first FOR statement selects the ROW "0" and final ROW in grid
			for c in range(len(grid[0])):					# For the two rows selected, Loop for how many columns in a ROW
				self.dfs(grid, r, c)						# Invoke DFS on each cell in the border rows
		for r in range(len(grid)):							# 2. Perform same function on Column "0" and final Column in grid
			for c in [0, len(grid[0])-1]:
				self.dfs(grid, r, c)
		for r in range(len(grid)):							# Final For loop to perform after DFS has changed border cells to "."
			for c in range(len(grid[0])):					# If not border and "O" change to "X", else if border change back to "O"
				if grid[r][c] == "O":
					grid[r][c] = "X"
				elif grid[r][c] == ".":
					grid[r][c] = "O"
		return grid
	def dfs(self, grid, r, c):
		if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "O":		# if the cells surrounding original is inbounds and a "O"
			grid[r][c] = "."														# change to "."
			self.dfs(grid, r + 1, c)
			self.dfs(grid, r - 1, c)
			self.dfs(grid, r, c +1)
			self.dfs(grid, r, c -1)


	def solveBFS(self, grid):
		q = collections.deque([])
		for r in range(len(grid)):																# This function checks if "O" on borders
			for c in range(len(grid[0])):														# Then appends cell to queue
				if (r in [0, len(grid)-1] or c in [0, len(grid[0]) -1]) and grid[r][c] == "O":	# When "[]" returns a boolean
					  q.append((r,c))															# if r in [0,3], not a range. It's if r = 0 or r = 3
	
		while q:
			row, col = q.popleft()
			if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "O":
				grid[row][col] = "."
				q.extend([(row-1, col), (row+1, col), (row, col-1), (row, col+1)])

		for r in range(len(grid)):
			for c in range(len(grid[0])):
				if grid[r][c] == "O":
					grid[r][c] = "X"
				elif grid[r][c] == ".":
					grid[r][c] = "O"
		return grid


Run = Solution()
Run.solveDFS(grid)

##############################
# Second Solution using DFS from comments - cleaner than the first version - possible runtime 90% 
##############################

# Cleaner:
	# Row, Col lengths are variables
	# DFS function takes only two parameters, No GRID.
		# Does this by including DFS function within "Solve" function.


grid = [
	["X", "X", "X", "X"],
	["X", "O", "O", "X"],
	["X", "X", "O", "X"],
	["X", "O", "X", "X"]
	]
class Solution:
	def solveDFS_v2(self, board):
		if not board or not board[0]:
			return []
		ROWS, COLS = len(board), len(board[0])

		def dfsBorder(r, c):
			if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == "O":
				board[r][c] = "T"
				dfsBorder(r + 1, c)
				dfsBorder(r - 1, c)
				dfsBorder(r, c + 1)
				dfsBorder(r, c - 1)
		
		# Invalidate border case
		for r in range(ROWS):
			for c in (0, COLS - 1):
				if board[r][c] == "O":
					dfsBorder(r,c)
		for c in range(1, COLS -1):
			for r in (0, ROWS -1):
				if board[r][c] == "O":
					dfsBorder(r,c)
		for r in range(ROWS):
			for c in range(COLS):
				if board[r][c] == "T":
					board[r][c] = "O"
				elif board[r][c] == "O":
					board[r][c] = "X"
		return board
Run = Solution()
Run.solveDFS_v2(grid)

####################
# Additional Grids
####################y

grid = [
	["X","X","X","X"],
	["X","O","O","X"],
	["X","X","O","X"],
	["X","O","X","X"]
]

grid = [
	["X", "X", "X"],
	["X", "O", "X"],
	["X", "X", "X"]
	]

grid = [
	["O", "O", "O"],
	["O", "O", "O"],
	["O", "O", "O"]
	]


#########################
# BFS and DFS examples taken from "edpresso"
#########################

# BFS
# Using a Dictionary, passing visited to BFS function
# Starting at selected "node"

class Solution:
	visited = []									# List to keep track of visited nodes
	queue = []					

	def bfs(visited, graph, node):
		visited.append(node)
		queue.append(node)

		while queue:
			s = queue.pop(0)

			for neighbour in graph[s]:				# Using a dictionary, thus what is popped from queue
				if neighbour not in visited:		# is then looked-up in dictionary
					visited.append(neighbour)
					queue.append(neighbour)


# DFS
# Using a Dictionary, passing visited to DFS function
# Starting at selected "node"

class Solution:
	visited = set()
	
	def DFS(self, visited, graph, node):
		if node not in visited:
			visited.add(node)
			for neighbour in graph[node]:
				self.DFS(visited, graph, neighbour)

#############################
#############################



# Remove duplicates - Remove when complete
class Solution:
	def pointer(self, words):
		
		i = 0
		
		for j in range(1, len(words)-1):
			if words[j] != words[i]:
				i += 1
				words[i] = words[j]
		return 1 + i


Run = Solution()
Run.pointer([1,2,2,3,4,5,6,6,7,7])


############
# Leetcode 1382

class Node:
	def __init__(self, val=0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def balanceBST(self, root):
		self.memo = []
		self.inorder(root)
		return self.memo


	def inorder(self, root):
		if root is None:
			return
		self.inorder(root.left)
		self.memo.append(root.val)
		self.inorder(root.right)



p7 = Node(10)
p6 = Node(5, p7)
p5 = Node(7, p6)
p8 = Node(8)
p4 = Node(15, p8)
p3 = Node(20, p4, p5)
p2 = Node(9)
Tree = Node(3, p2, p3)

Run = Solution()
Run.balanceBST(Tree)



###############



