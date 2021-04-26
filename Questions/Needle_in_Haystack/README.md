

## Two Pointers - Slow
- Return type is list of `booleans`
- Enumerate not needed in this example
```python
def camelMatch(self, queries, pattern):
    def patternMatch(p, q):
        i = 0
        for key, val in enumerate(q):
            if i < len(p) and p[i] == val:
                i += 1
            elif val.isupper():
                return False
        return i == len(p)
    return [patternMatch(pattern, q) for q in queries]
```

## Two Pointers - Second closing pointer
```python
def prefix(business_names, searchTerm):
    split = [i.split() for i in business_names]
    ans = []
    for name in split:
        for i in range(len(name)):
            query = ' '.join(name[i:])
            if query.startswith(searchTerm):
                ans.append(name)
                break
    aa = [' '.join(i) for i in ans]
    print(aa)
```