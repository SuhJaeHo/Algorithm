class Solution:
    def decodeString(self, s: str) -> str:
        res = ""

        repeatStack = []
        stringStack = []

        repeat = ""

        for i in range(len(s)):
            char = s[i]

            if char.isdigit():
                repeat += char
            elif char == "[":
                repeatStack.append(repeat)
                stringStack.append("")
                repeat = ""
            elif char == "]":
                repeatCnt = repeatStack.pop()
                string = stringStack.pop()

                if stringStack:
                    stringStack[-1] += string * int(repeatCnt)
                else:
                    res += string * int(repeatCnt)
            else:
                if stringStack:
                    stringStack[-1] += char
                else:
                    res += char

        return res

# res = Solution().decodeString("3[a]2[bc]")
# res = Solution().decodeString("3[a2[c]]")
res = Solution().decodeString("2[abc]3[cd]ef")
print("res", res)
