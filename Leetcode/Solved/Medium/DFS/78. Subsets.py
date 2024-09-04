from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def gen(acc: List[int], startIdx: int):
            for i in range(startIdx, len(nums)):
                acc += [nums[i]]
                res.append(acc.copy())
                gen(acc, i + 1)
                acc.pop()

        gen([], 0)

        return res

res = Solution().subsets([1,2,3])
print("res", res)
