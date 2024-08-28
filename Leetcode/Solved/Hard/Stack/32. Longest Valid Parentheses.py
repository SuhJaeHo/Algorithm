class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0

        openBracketStack = []
        closeBracketStack = []
        for i in range(len(s)):
            if s[i] == "(":
                openBracketStack.append(i)
            else:
                if openBracketStack:
                    openBracketStack.pop()
                else:
                    closeBracketStack.append(i)

        unBalancedBracketIndices = sorted(openBracketStack + closeBracketStack)

        if len(unBalancedBracketIndices) == 0:
            return len(s)

        left = 0
        for i in range(len(unBalancedBracketIndices)):
            res = max(res, unBalancedBracketIndices[i] - left)
            left = unBalancedBracketIndices[i] + 1

        if unBalancedBracketIndices:
            res = max(res, len(s) - (unBalancedBracketIndices[-1] + 1))

        return res

"""
Typical Solution
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len

# res = Solution().longestValidParentheses("(()")
# res = Solution().longestValidParentheses(")()())(()")
# res = Solution().longestValidParentheses("()(()")
# res = Solution().longestValidParentheses("(())")
# res = Solution().longestValidParentheses("(()())")
res = Solution().longestValidParentheses("()")
print("res", res)
