"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/grumpy-bookstore-owner/description/
"""


from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        win_of_make_satisfied = satisfied = max_make_satisfied = 0
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            satisfied += (1 - g) * c
            win_of_make_satisfied += g * c
            if i >= X and grumpy[i - X] == 1:
                win_of_make_satisfied -= customers[i - X]
            max_make_satisfied = max(win_of_make_satisfied, max_make_satisfied)
        return satisfied + max_make_satisfied
