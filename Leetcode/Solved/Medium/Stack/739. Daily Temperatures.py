from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prevIdx = stack.pop()
                res[prevIdx] = i - prevIdx
            stack.append(i)

        return res

res = Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
print("res", res)
