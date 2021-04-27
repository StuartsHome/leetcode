

class Trie:
    def __init__(self):
        self.memo = memo


    def insert(self, words):
        curr = self.memo
        for char in words:
            if char in curr:
                curr[char] = {}
            curr = curr[char]
        curr["#"] = True