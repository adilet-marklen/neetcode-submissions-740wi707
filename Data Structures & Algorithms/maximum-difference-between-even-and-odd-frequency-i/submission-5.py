class Solution:
    def maxDifference(self, s: str) -> int:
        hashset = {}

        for ch in s:
            hashset[ch] = hashset.get(ch, 0) + 1
        
        odd, even = [], []

        for v in hashset.values():
            if v % 2 != 0:
                odd.append(v)
            else:
                even.append(v)

        return max(odd) - min(even)
        