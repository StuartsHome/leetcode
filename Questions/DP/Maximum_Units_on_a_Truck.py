# Leetcode ?. Maximum Units on a Truck
# T: O(n)
# S: O(n)

class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse = True)
        total = 0
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            if truckSize - boxTypes[i][0] > 0:
                truckSize -= boxTypes[i][0]
                total += boxTypes[i][0] * boxTypes[i][1]
            else:
                total += truckSize * boxTypes[i][1]
                truckSize -= truckSize
                return total
            i += 1
        return total

        """
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse = True)
        total = 0
        for boxes, j in boxTypes:
            boxes = min(boxes, truckSize)
            total += boxes * j
            truckSize -= boxes
            if truckSize==0:
                break
        return total
        """

Run = Solution()
Run.maximumUnits([[5,10],[2,5],[4,7],[3,9]],10)
([[1,3],[2,2],[3,1]], 4)