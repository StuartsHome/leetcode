# Leetcode 12. Integer to Roman

class Solution:
    def intToRoman(self, num):
        dict = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for letter, n in zip(dict, nums):
            result += letter * int(num / n) # tells you how many times n occurs in num
            num %= n                        # then removes n from num e.g. 1 occurs in 3 three times, it removes 3
        return result

Run = Solution()
Run.intToRoman(58)