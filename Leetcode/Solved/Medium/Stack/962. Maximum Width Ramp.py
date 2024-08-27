from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0

        stack = [[nums[0], 0]]

        for i in range(1, len(nums)):
            [val, idx] = stack[-1]
            if nums[i] >= val:
                res = max(res, i - idx)
            else:
                stack.append([nums[i], i])

        print("stack", stack)

        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1][0] <= nums[i]:
                val, idx = stack.pop()
                res = max(res, i - idx)

        # for i in range(len(nums) - 1, -1, -1):
        #     for val, idx in stack:
        #         if nums[i] >= val:
        #             res = max(res, i - idx)
        #             break

        return res

"""
Typical Solution
"""
# class Solution:
#     def maxWidthRamp(self, nums: List[int]) -> int:
#         res = 0

#         stack = []
#         n = len(nums)

#         for i in range(n):
#             if not stack or nums[i] < nums[stack[-1]]:
#                 stack.append(i)

#         for i in range(n - 1, -1, -1):
#             while stack and nums[i] >= nums[stack[-1]]:
#                 res = max(res, i - stack.pop())

#         return res

# res = Solution().maxWidthRamp([6,0,8,2,1,5])
res = Solution().maxWidthRamp([9,8,1,0,1,9,4,0,4,1])

# res = Solution().maxWidthRamp([3,6,2,8,1,1])
# res = Solution().maxWidthRamp([6,7,4,5,2,2,2,4])
print("res", res)
