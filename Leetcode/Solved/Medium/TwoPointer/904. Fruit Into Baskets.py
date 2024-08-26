from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0

        if len(fruits) <= 2:
            res = max(res, len(fruits))
        else:
            res = 2

        left = 0
        hmCnt = Counter(fruits[:2])

        for i in range(2, len(fruits)):
            if hmCnt.get(fruits[i]):
                hmCnt[fruits[i]] += 1
            else:
                hmCnt[fruits[i]] = 1

            if len(hmCnt.keys()) <= 2:
                res = max(res, sum(hmCnt.values()))

            else:
                if hmCnt[fruits[left]] == 1:
                    del hmCnt[fruits[left]]
                else:
                    hmCnt[fruits[left]] -= 1
                left += 1

        return res

# res = Solution().totalFruit([1,2,1])
# res = Solution().totalFruit([0,1,2,2])
res = Solution().totalFruit([0,1,2])
print("res", res)
