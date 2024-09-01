from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        nums = [i + 1 for i in range(n)]

        def gen(acc: List[int], start: int):
            if len(acc) == k:
                res.append(acc.copy())
                return

            for i in range(start, len(nums)):
                acc += [nums[i]]
                gen(acc, i + 1)
                acc.pop()

        gen([], 0)

        return res

# res = Solution().combine(4, 2)
res = Solution().combine(5, 3)
print("res", res)
