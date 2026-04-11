class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_map = {}

        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
        
        return not all(v == 1 for v in num_map.values())
        