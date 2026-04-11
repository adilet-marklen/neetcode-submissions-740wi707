class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashset = {}
        uniq = []

        for l in arr:
            hashset[l] = hashset.get(l, 0) + 1
        
        for l in arr:
            if hashset[l] == 1:
                uniq.append(l)
        
        if len(uniq) < k:
            return ""
        else:
            return uniq[k - 1]

