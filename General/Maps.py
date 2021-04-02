# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))