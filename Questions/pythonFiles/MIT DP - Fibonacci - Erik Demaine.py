# MIT DP - Fibonacci - Erik Demaine

# Contents
	# Naive Recursion
	# DP with dictionary - function calls
	# Bottom up DP - for loop, no function calls


# for any DP
# the run time is equal to
# number of different sub problems you solve
# * the amount of time spent per sub problem
# when you measure time per sub problem
# you ignore recursive calls, because we don't have to solve recurences with DP




# Fibonacci numbers - Naive Recursive
	# recursively call n-1 and n-2, then add together to get F, return F
	# TimeComplexity: Exponential Time
	# T(n) = T(n-1) + T(n-2) + 0(1)
	# Time of input = First compute N-1 fibonacci number and then the N-2 Fibonacci number
		# Then take a constant time from the additions, comparisons, return. All take constant time.
def fibonacci(n):
	if n <= 2:
		f=1
	else:
		f = fibonacci(n-1) + fibonacci(n-2)
	return f

fibonacci(10)

# Fibonacci Numbers - Dynamic Programming
# can be done in logN, but this algorithm is linear - 0(N)
# it's linear because there is N non-memoized calls, and each of them costs constant, it's a product of N * 0(1)

# DP = recursion + memoization
# DP is memoize (remember) 
# and reuse solutions to subproblems that
# help solve the problem.

# memoization is, once solve sub problem.
# write down answer,
# if you need to solve same sub problem again
# reuse the answer


# whenever compute fibonacci number, put in dicitionary
# then when we need to compute nth fibonacci number, we check if it is already in the dictionary?
# did we already solve this problem? If so, return that answer. Otherwise, compute it.

# First we create empty dictionary.
# check if fn is already in the dictionary.
	# if the key is in the dictionary, we return the corresponding value in the dictionary
# once we computed nth fibonacci number, we store it in memo dictionary
# if we ever need to compute f of n again, we return the value


# recursion Tree
# dictionary stores values, so not computed again
# source: Eric Demain MIT lecture Recursion

# recursion doesn't store values already computed (as can be seen in recursion table)
# DP, stores values so not computed again

# the fibonacci function is called once.
# you only make recursive calls the first time you call the function.
# after, the value is in the memo dictionary and the function will not recurse.

# There are two times fibonacci is called:
	# The first time with no dictionary, and does recursion
	# everytime after, you're doing memorized calls that cost CONSTANT TIME (basically free)
	# memoized calls cost 0(1)
	# the number of non-memoized calls (first time calling function) is N
# Non recursive work per call of the function is constant 0(1)
# therefore, the running time is linear 0(n)
# Linear is better than exponential
# To calculate time complexity of memoization algorithm: multiply number of sub-problems
# by time of sub-problem



memo = {}
def fibonacci(n):
	if n in memo:
		return memo[n]
	if n <= 2:
		f=1
	else:
		f = fibonacci(n-1)+fibonacci(n-2)
	memo[n] = f
	print(memo)
	return f

fibonacci(10)


# for dynamic programming
# the number of array depends on the variables for the function
# e.g. this function takes two variables, so the answer is a 2D array

#################################

# Recursive algorithm starts at the top of the recursion tree,
# and works its way down
# you can do the reverse
# Start at the bottom and work way up
# instead of function calls, they are lookups into a table



# Bottom-up DP algorithm
k = 5
fib = {}
for n in range(1, k+1):
	if n <= 2:
		f = 1
	else:
		f = fib[n-1] + fib[n-2]
	fib[n] = f
	print(fib[n])

# Bottom up - same computations as memoized version
# Topological sort of subproblem dependency dag

# subproblem dependencies should be acyclic, otherwise you get an infinite algorithm
# for memoization to work and DP, this is what you need.
# if it's cyclic, you 

# To do a bottom up algorithm you do a topological sort of the subproblem dependency DAG