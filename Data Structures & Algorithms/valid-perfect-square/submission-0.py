class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return 0

        l, r = 0, num
        res = 0

        while l <= r:
            m = (l + r) // 2
            if m ** 2 == num:
                return True
            elif m ** 2 < num:
                res = m
                l = m + 1
            else:
                r = m - 1
        return False
            