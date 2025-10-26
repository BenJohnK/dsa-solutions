from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        import sys
        highest = -sys.maxsize
        sum = 0
        for x in nums:
            sum = sum + x
            if sum > highest:
                highest = sum
            if sum < 0:
                sum = 0
        return highest