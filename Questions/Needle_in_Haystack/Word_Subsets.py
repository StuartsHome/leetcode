# Leetcode 916. Word Subsets
# Second step is for each string a from A calculate counter and check
# that it is bigger for each element than "cnt".
# This can be done using  "not"


from collections import Counter
class Solution:
    def wordSubsets(self, A, B):
        cnt = Counter()
        for b in B:
            cnt |= Counter(b)
        
        return [a for a in A if not cnt - Counter(a)]

        # Solution 1 . same as first solution, but not using the ("or" pipe)
        """ 
        for ix,i in enumerate(A):
            A[ix]=(i,Counter(i))
        exp=Counter()
        for i in B:
            c=Counter(i)
            for j in c:
                if j in exp:
                    exp[j]=max(exp[j],c[j])
                else:
                    exp[j]=c[j]
        # print(exp)
        res=[]
        for org,i in A:
            if i&exp == exp:
                res.append(org)
        return res
        """

        # Solution 1.
        # Construct unique subset for B
        """
        s = set(A)
        required = {}
        for i in B:
            for j in i:
                count = i.count(j)
                if j not in required or count > required[j]:
                # Instead of If statement can use the below
                # max(i.count(j), required.get(char, 0))
                    required[j] = count
        # print(required)
        for i in A:
            for j in required:
                if i.count(j) < required[j]:
                    s.remove(i)
                    break
        return list(s)
        """

Run = Solution()
Run.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["lo","eo"])
(["amazon","apple","facebook","google","leetcode"],["e","oo"])
(["amazon","apple","facebook","google","leetcode"], ["ec","oc","ceo"])

