class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for i in s:
            count[i] = count.get(i, 0) + 1
        for i in t:
            count[i] = count.get(i, 0) - 1
        return all(v == 0 for v in count.values())
        