# Leetcode 1507. Reformat Date

class Solution:
    def reformatDate(self, date):
        memo = {
            "Jan" : "01",
            "Feb" : "02",
            "Mar" : "03",
            "Apr" : "04",
            "May" : "05",
            "Jun" : "06",
            "Jul" : "07",
            "Aug" : "08",
            "Sep" : "09",
            "Oct" : "10",
            "Nov" : "11",
            "Dec" : "12"
        }
        aa = date.split()
        aa[1] = memo[aa[1]]
        N = len(aa[0])
        aa[0] = aa[0][:N-2]
        if len(aa[0]) == 1:
            aa[0] = "0" + aa[0]
        aa = aa[2] + "-" + aa[1] + "-" + aa[0]
        return aa

Run = Solution()
Run.reformatDate("6th Jun 1933")
("20th Oct 2052")