class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
                if current > maximum:
                    maximum = current
            elif num == 0:
                current = 0
        return maximum