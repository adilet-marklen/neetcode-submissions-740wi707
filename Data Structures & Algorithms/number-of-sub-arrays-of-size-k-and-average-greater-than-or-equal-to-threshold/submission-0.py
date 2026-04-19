class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
     
        for L in range(len(arr) - k + 1):
            if sum(arr[L:L+k])/k >= threshold:
                res += 1
        return res