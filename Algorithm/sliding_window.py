"""
A window is a subset of elements from the array.
While slides over the array,
iterate through the data and update the window by adding next element and remove the leftmost one.
"""

"""
567. Permutation in String
"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L, l = len(s1) - 1, 0
        cnt1, cnt2 = Counter(s1), Counter(s2[:L])

        for _, char in enumerate(s2[L:]):
            cnt2[char] += 1
            if cnt1 == cnt2: return True
            cnt2[s2[l]] -= 1
            l += 1

        return False

Solution().checkInclusion("ab", "eidbaooo")
Solution().checkInclusion("ab", "eidboaoo")
