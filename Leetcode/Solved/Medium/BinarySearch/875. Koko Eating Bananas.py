from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 1e9

        piles.sort()

        l = 1
        r = piles[-1]

        while l <= r:
            mid = (l + r) // 2

            hour = 0
            for pile in piles:
                if pile % mid != 0:
                    hour += pile // mid + 1
                else:
                    hour += pile // mid

            if hour > h:
                l = mid + 1
            else:
                res = int(min(res, mid))
                r = mid - 1

        return res

# res = Solution().minEatingSpeed([3,6,7,11], 8)
# res = Solution().minEatingSpeed([30,11,23,4,20], 5)
res = Solution().minEatingSpeed([1000000000,1000000000], 3)
print("res", res)
