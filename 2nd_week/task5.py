"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/description/
"""


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        swap_x, swap_y = 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == "x":
                    swap_x += 1
                else:
                    swap_y += 1

        if (swap_x + swap_y) % 2 == 1:
            return -1

        res = swap_x // 2 + swap_y // 2
        if swap_x % 2 == 1 and swap_y % 2 == 1:
            res += 2

        return res
