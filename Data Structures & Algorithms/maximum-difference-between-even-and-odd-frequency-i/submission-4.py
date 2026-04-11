class Solution:
    def maxDifference(self, s: str) -> int:
        hashset = {}

        for ch in s:
            hashset[ch] = hashset.get(ch, 0) + 1
        
        a1 = max(v for v in hashset.values() if v % 2 != 0)
        a2 = min(v for v in hashset.values() if v % 2 == 0)

        diff = a1 - a2
        return diff
        