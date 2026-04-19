class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = threshold * k
        res = 0
        window_sum = sum(arr[:k])

        if window_sum >= target:
            res += 1
        
        for i in range(k, len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i - k]

            if window_sum >= target:
                res += 1
                
        return res