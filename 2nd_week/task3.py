"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/decode-string/description/
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = 0
        ans = ""
        for c in s:
            if c == "[":
                stack.append(ans)
                stack.append(curr)
                ans = ""
                curr = 0
            elif c == "]":
                num = stack.pop()
                prev = stack.pop()
                ans = prev + num * ans
            elif c.isdigit():
                curr = curr * 10 + int(c)
            else:
                ans += c
        return ans
