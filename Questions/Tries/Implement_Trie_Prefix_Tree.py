# Leetcode 208. Implement Trie (Prefix Tree)

class Trie:
    def __init__(self):
        self.memo = {}

    def insert(self, word):
        current = self.memo
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current['#'] = True         # #' marks the end of word

    def search(self, word):
        current = self.memo
        for char in word:
            if char not in current:
                return False
            current = current[char]
        if '#' in current:
            return True
        return False


    def startsWith(self, prefix):
        current = self.memo
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True

obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_3 = obj.startsWith("app")
param_4 = obj.search("ape")
