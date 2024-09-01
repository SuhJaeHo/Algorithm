from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        used = [False] * len(nums)

        def gen(acc: List[int], used: List[bool]):
            if len(acc) == len(nums):
                res.append(acc.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    acc.append(nums[i])
                    used[i] = True
                    gen(acc, used)
                    acc.pop()
                    used[i] = False

        gen([], used)

        return res

res = Solution().permute([1,2,3])
print("res", res)
