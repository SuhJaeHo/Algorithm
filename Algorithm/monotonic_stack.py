"""
The key idea behind monotonic stack is to use the stack to keep track of elements
that have not yet found their desired smaller or larger element
"""

"""
503. Next Greater Element II
"""
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)

        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)

        return res

Solution().nextGreaterElements([2,1,2,4,3])
