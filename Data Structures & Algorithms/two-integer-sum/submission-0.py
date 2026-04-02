class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        known_numbers = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in known_numbers:
                return [known_numbers[diff], idx]
            known_numbers[num] = idx
        