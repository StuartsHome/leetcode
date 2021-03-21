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
(n & (n-1) == 0) and n != 0