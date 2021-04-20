# Leetcode 43. Multiply Strings
# You can use the ord() function to calculate the value assigned 
# to the particular digit and subtract it from the ord() value of 0, which will be the resultant digit.

# Start from right to left, perform multiplication on every pair of digits, and add them together.

class Solution:
    def multiply(self, num1, num2):
        product = [0] * (len(num1) + len(num2))
        pos = len(product)-1
        
        for n1 in reversed(num1):
            tempPos = pos
            for n2 in reversed(num2):
                product[tempPos] += int(n1) * int(n2)
                product[tempPos-1] += product[tempPos]//10
                product[tempPos] %= 10
                tempPos -= 1
            pos -= 1

        # Remove leading zeroes   
        pt = 0
        while pt < len(product)-1 and product[pt] == 0:
            pt += 1

        # from last zero onwards, convert int to string and join into one string
        return ''.join(map(str, product[pt:]))

"""        
        n, m = len(num1), len(num2)
        if not n or not m:
            return "0"
        
        result = [0] * (n + m)
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                current = int(result[i + j + 1]) + int(num1[i]) * int(num2[j])
                result[i + j + 1] = current % 10
                result[i + j] += current // 10
        
        for i, c in enumerate(result):
            if c != 0:
                return "".join(map(str, result[i:]))
        
        return "0"
        """
Run = Solution()
Run.multiply("123","456")


class Solution:
    def multiply(self, num1, num2):
        res1, res2 = 0, 0 
        for d in num1:
            res1 = res1 * 10 + (ord(d) - ord('0'))
        for d in num2:
            res2 = res2 * 10 + (ord(d) - ord('0'))
        return str(res1 * res2)