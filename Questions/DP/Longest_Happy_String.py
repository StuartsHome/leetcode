
class Solution:
    def longestDiverseString(self, a, b, c):
        # string = [[a, 'a'],[b, 'b'], [c, 'c']]                      # list instead of dict to be able to sort on count
        # ans = []

        # while True:
        #     string.sort()                                            # sort to order by count,and take greatest count from end each turn
        #     if len(ans) >= 2 and ans[-2] == ans[-1] == string[2][1]: # if the last 2 characters in ans are c's
        #         i = 1
        #     else:
        #         i = 2
        #     if string[i][0]:
        #         ans.append(string[i][1])
        #         string[i][0] -= 1
        #     else:
        #         break
        # return "".join(ans)
        available = {'a':a, 'b':b, 'c':c}
        ans = ["#", "#"]
        while sum(available.values()) > 0:
            pick_max_available = ''
            for ch in available.keys():
                if available[ch] > 0 and ans and not (ans[-1] == ch and ans[-2] == ch): # Pick a key from available, if the count > 0 and not the last 2 chars in ans
                    if not pick_max_available:
                        pick_max_available = ch
                    elif available[ch] > available[pick_max_available]:
                        pick_max_available = ch
            if not pick_max_available:
                break
            ans += [pick_max_available]
            available[pick_max_available] -= 1
            
        return ''.join(ans[2:])


Run = Solution()
Run.longestDiverseString(1,1,7)