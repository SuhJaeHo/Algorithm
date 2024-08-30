from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []

        left = 0
        right = len(numbers) - 1

        while left < right:
            val = numbers[left] + numbers[right]
            if val == target:
                res += [left + 1] + [right + 1]
                break
            elif val > target:
                right -= 1
            else:
                left += 1

        return res

res = Solution().twoSum([2,7,11,15], 9)
print("res", res)
