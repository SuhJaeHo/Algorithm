from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1

# res = Solution().search([-1,0,3,5,9,12], 9)
# res = Solution().search([-1,0,3,5,9,12], 2)
res = Solution().search([5], 5)
print("res", res)
