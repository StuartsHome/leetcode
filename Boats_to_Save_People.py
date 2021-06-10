# Leetcode 881. Boats to Save People

# T: O(n log n), where n is the len(people)
# S: O(n)

class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        result = 0
        i, j = 0, len(people) -1
        while i <= j:
            result += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return result


Run = Solution()
Run.numRescueBoats([3,2,2,1], 3)