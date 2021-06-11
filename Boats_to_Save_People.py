# Leetcode 881. Boats to Save People

# Two pointer greedy solution - i.e. at each step find the best solution
# T: O(n log n), where n is the len(people)
# S: O(n)

# If the heaviest person can share a boat with the lightest person, then
# do so. Otherwise, the heaviest person can't pair with anyone, so they 
# get their own boat.

# The reason this works is because if the lightest person can pair with
# anyone, they might as well pair with the heaviest person.

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