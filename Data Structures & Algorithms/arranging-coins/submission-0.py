class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0

        while l <= r:
            m = (l + r) // 2
            total = m * (m + 1) / 2
            if total == n:
                return m
            elif total < n:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res