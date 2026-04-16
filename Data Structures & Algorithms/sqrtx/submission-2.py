class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        l, r = 0, x
        res = 0

        while l <= r:
            m = (l + r) // 2
            if m ** 2 == x:
                return m
            elif m ** 2 > x:
                r = m - 1
            else:
                res = m
                l = m + 1
        return res

