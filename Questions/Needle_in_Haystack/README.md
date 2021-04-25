

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