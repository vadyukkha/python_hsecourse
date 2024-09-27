"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/equal-rational-numbers/description/
"""

from fractions import Fraction as F


class Solution:
    def str_to_int(self, s):
        if "." not in s:
            return F(int(s), 1)

        index = s.index(".")
        ans = F(int(s[:index]), 1)
        s = s[index + 1 :]
        if "(" not in s:
            if s:
                ans += F(int(s), 10 ** len(s))
            return ans

        ind = s.index("(")
        if ind > 0:
            ans += F(int(s[:ind]), 10**ind)

        s = s[ind + 1 : -1]
        ans += F(int(s), 10**ind * (10 ** len(s) - 1))
        return ans

    def isRationalEqual(self, s: str, t: str) -> bool:
        return self.str_to_int(s) == self.str_to_int(t)
