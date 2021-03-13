# Leetcode 706. Design HashMap

class MyHashMap:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.memo = {}
        

    def put(self, key, value):
        if key in self.memo:
            del self.memo[key]
            self.memo[key] = value
            return self.memo
        else:
            self.memo[key] = value
            return self.memo

    def get(self, key):
        if key in self.memo:
            return self.memo[key]
        else:
            return -1

    def remove(self, key):
        if key in self.memo:
            del self.memo[key]
        else:
            return -1



Obj = MyHashMap()
Obj.put(1, 20)
print(Obj)
