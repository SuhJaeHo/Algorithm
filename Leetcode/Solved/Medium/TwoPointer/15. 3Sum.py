from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        hm = {}
        nums.sort()

        for i in range(len(nums) - 2):
            acc = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                acc += nums[left] + nums[right]
                if acc == 0:
                    key = str(nums[i]) + str(nums[left]) + str(nums[right])
                    if not hm.get(key):
                        res.append([nums[i], nums[left], nums[right]])
                        hm[key]= True

                    left += 1
                    right -= 1
                elif acc > 0:
                    right -= 1
                else:
                    left += 1

                acc = nums[i]

        return res

res = Solution().threeSum([-1,0,1,2,-1,-4])
print("res", res)
