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
        """
        s = set(A)
        letters_required = {}
        for i in B:
            for j in i:
                count = i.count(j)
                if j not in letters_required or count > letters_required[j]:
                    letters_required[j] = count

        for i in A:
            for j in letters_required:
                if i.count(j) < letters_required[j]:
                    s.remove(i)
                    break
        return list(s)
        """

Run = Solution()
Run.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["lo","eo"])
(["amazon","apple","facebook","google","leetcode"],["e","oo"])
(["amazon","apple","facebook","google","leetcode"], ["ec","oc","ceo"])

