# This file is to test the use of Lambdas and show their functionality


# Simple Lambda
x = lambda a : a + 10
print(x(5))

# Multiple arguments and parameters
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Lambda on 2D array
sorted_list = sorted([[0,1],[0,2][1,1],[2,1]], key=lambda x : x[0])
print(sorted_list)

######
# From Geeks for Geeks
######

# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y*y*y
  
lambda_cube = lambda y: y*y*y
  
# using the normally
# defined function
print(cube(5))
  
# using the lamda function
print(lambda_cube(5))

