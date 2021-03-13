

class Solution:
    def thousandSeparator(self, n):

        # code from discussions
        s=str(n)
        s=s[::-1]
        #res = '.'.join(s[i:i + 3] for i in range(0, len(s), 3))
        yy = (s[i:i + 3] for i in range(0, len(s), 3))
        xx = '.'.join(yy)


Run = Solution()
Run.thousandSeparator(123456789)
(1234)

987

        # temp_n = list(str(n))
        # counter = 0
        # result = ""
        # for i in reversed(temp_n):
            
        #     if counter / 3 == 1:
        #         result = "." + result
        #     aa = len(result)
        #     result = i + result
        #     counter += 1
            
        # print(result)