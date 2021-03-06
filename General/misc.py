knights = {'word': 1, 'sentence': 2, 'paragraphs': 3}
for k, v in knights.items():
    print(k, v)

print(list(knights))
print(knights)

# Sorting on len of Dict

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(key=len)
print(cars)


# returning on max len
#return max(arr, key=len)


# removing id from dict whether or not it exsits
dict.pop(id, None)


# default dict
from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
    
# set default_factory (default dict) to int
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

sorted(d.items())

# set default_factory to set
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)

sorted(d.items())

# Power of two
# every power of 2 has exactly 1 bit set to 1 (the bit in that number's log base-2 index).
(n & (n-1) == 0) and n != 0

# Factors of number
def factors(x):
    return [i for i in range(1,x+1) if x%i==0]

def factors(n):
    return set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )

def factors(n):
    results = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            results.add(i)
            results.add(int(n/i))
    return results

# Unpacking an iterable into arguments
times = [10, 20, 30, 40, 50]
print(*times)

# Dictionary - keys and values
for i in d:
    print (i, d[i])

# For Python3
for k, v in d.items():
    print(k, v)

# Max and min values
float('inf')
float('-inf')

# Square Root
x = 10
x**.5


# Using Dictionary - min or max of values:
dictionary = {}
aa = min(dictionary, key=dictionary.get)

# Using Dictionary - sort values:
memo = sorted(memo.items(), key=lambda x: x[1])


# DP arrays - don't do this! Do this:
dp = [[False] * n for _ in matrix] # Good
dp = [[False] * n]*m               # Bad - every value in first row replicates to all rows