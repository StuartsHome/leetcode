# Leetcode 406. Queue Reconstruction by Height
# T: O(n^2) - Loop over people once, and each insertion is O(n)
# S: O(n)

# Sort people in order of descending height
# If multiple people of same height, sort them in ascending order
# of the number of people in front of them.

class Solution:
    def reconstructQueue(self, people):
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

Run = Solution()
Run.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])

[5,0], [7,0], [7,1]