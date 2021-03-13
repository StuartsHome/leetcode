# Roman to Int

class Solution:
    def romanToInt(self, s):
        memo = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        val = 0
        for i in range(0, len(s) - 1):
            if memo[s[i]] < memo[s[i+1]]:
                    val -= memo[s[i]]
            else:
                val += memo[s[i]]
        val += memo[s[-1]]
        print(val)

Run = Solution()
Run.romanToInt("III")

("MCMXCIV")

("IV")
("LVIII")
