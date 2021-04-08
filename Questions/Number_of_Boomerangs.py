# Leetcode 447. Number of Boomerangs.
# At each point i, create a hashmap memo of the form {d:n}
# where n is the total number of points that are d distance from p
# Then we only need to count the number of unique pairs of those points.
# The key insight here is that if we have a list of n points [p1, p2, p3, ..., pn]
# then there are nP2 = (n! / (n-2)!) = n*(n-1) pairs of points that can follow p in order to form a boomerang.

# For every point, there are k points with distance d, so there are k*(k-1) pairwise with distance d.
# Permutation formula, to pick 2 out of k elements, the number of combinations is:
# A_(k)^(m=2) = k(k-1)(k-2)(k-m+1) = k(k-2+1) = k(k-1)
# Which is:
"""
# Sum the total number of combinations for point
for count in distance_count.values():
    result += count * (count - 1)
"""

# Euclidean distance
# Using the Pythagorean theorem to compute two-dimensional Euclidean distance
# d(p,q)**2 = (q1 - p1)**2 + (q2-p2)**2
# Basically you have two points and your calculating the third

# My notes:
"""
n*(n-1) is displayed in two different ways in the solutions below:
1. 
This solution is not adding to count when the distanced is stored in memo first.
But subsequently adds a[c] to count every time it is then found
c = (i[0]-j[0])**2+(i[1]-j[1])**2 
if c not in a:
    a[c]=1
else:
    count += a[c]  
    a[c]+=1      

2. 
"""


class Solution:
    def numberOfBoomerangs(self, points):
        count = 0
        for i in points:
            a={}
            for j in points:
                c = (i[0]-j[0])**2 + (i[1]-j[1])**2  # Squared for euclidean distance between 2 points
                if c not in a:
                    a[c]=1
                else:
                    count += a[c]  
                    a[c]+=1       ### to find the number of all combinations
        return count*2   # Multiply by 2 because [a,b,c] and [a,c,b] are two different cases.

    # Solution 2
    """
    def get_distance(p1,p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res=0
        for i in range(len(points)):
            dic={}
            for j in range(len(points)):
                if i ==j:
                    continue
                d = get_distance(points[i],points[j])
                if d not in dic:
                    dic[d] =1
                else:
                    dic[d] +=1
            for key,value in dic.items():
                print(value)
                res = value *(value-1) + res // 
        return res
    """

    # Solution 3 - Simplest - O(n^2)
    """
        n = 0
        for a,b in points:
            counter = {}
            for x,y in points:
                # NOTE: x,y == a,b can only be registered once, so...
				#       radius=0 never has enough points to make a false triplet
                key = (x-a)**2 + (y-b)**2
                if key in counter:
                    n += 2*counter[key]
                    counter[key] += 1
                else:
                    counter[key] = 1
        return n
    """

    # Solution 4 - Slowest - using Get method of hash table
    """
        count = 0
        for i in range(len(points)):
            memo = {}
            for j in range(len(points)):
                if i != j:
                    dt = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2)
                    count += memo.get(dt, 0)
                    memo[dt] = memo.get(dt, 0) + 1
        return count*2 # Multiply by 2 because [a,b,c] and [a,c,b] are two different cases.
    """


Run = Solution()
Run.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])
# Expected 5
([[0,0],[1,0],[2,0]])