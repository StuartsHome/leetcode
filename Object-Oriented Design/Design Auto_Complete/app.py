
# Trie data structure

class Trie:
    def __init__(self):
        self.memo = {}

    def insert(self, word):
        curr = self.memo
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['#'] = True

    def search(self, word):
        curr = self.memo
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        if '#' in curr:
            return True
        return False

    def startsWith(self, prefix):
        curr = self.memo
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True


Request = Trie()
Request.insert("hello")
Request.startsWith("hel")


import unittest
import unittest.mock
from unittest.mock import Mock, patch
class Test(unittest.TestCase):

    mock = Mock()
    mock.memo = {"h": {"e": {"l": {"l": {"o": {"#" : True}}}}}}

    def test_startswith(self):
        t = Trie()
        t.insert("hello")
        start = t.startsWith("hel")
        self.assertTrue(start, True)


