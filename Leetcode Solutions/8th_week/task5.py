"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/get-equal-substrings-within-budget/description/
"""


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        st = 0
        curr = 0
        mx_ln = 0

        for end in range(len(s)):
            curr += abs(ord(s[end]) - ord(t[end]))

            while curr > maxCost:
                curr -= abs(ord(s[st]) - ord(t[st]))
                st += 1

            mx_ln = max(mx_ln, end - st + 1)

        return mx_ln
