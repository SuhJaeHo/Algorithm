from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1

        hmCnt = defaultdict(int)

        left = 0
        maxCntChar = s[0]
        hmCnt[maxCntChar] += 1

        for i in range(1, len(s)):
            char = s[i]
            hmCnt[char] += 1

            if maxCntChar != char and hmCnt[maxCntChar] < hmCnt[char]:
                maxCntChar = char

            if (i + 1 - left) - hmCnt[maxCntChar] > k:
                hmCnt[s[left]] -= 1
                left += 1
            else:
                res = max(res, i + 1 - left)

        return res

# res = Solution().characterReplacement("ABAB", 2)
# res = Solution().characterReplacement("AABABBA", 1)
res = Solution().characterReplacement("AAAA", 0)
# res = Solution().characterReplacement("ABAA", 0)
print("res", res)
