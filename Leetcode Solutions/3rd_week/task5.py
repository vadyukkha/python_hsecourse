"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/contains-duplicate-iii/description/
"""


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: list[int], indexDiff: int, valueDiff: int
    ) -> bool:
        table = {}
        for i, n in enumerate(nums):
            basket = n // (indexDiff + 1)

            if basket in table and i - table[basket][0] <= indexDiff:
                return True

            if basket - 1 in table:
                prev_basket = table[basket - 1]
                if (
                    i - prev_basket[0] <= indexDiff
                    and abs(n - prev_basket[1]) <= valueDiff
                ):
                    return True

            if basket + 1 in table:
                next_basket = table[basket + 1]
                if (
                    i - next_basket[0] <= indexDiff
                    and abs(n - next_basket[1]) <= valueDiff
                ):
                    return True

            table[basket] = (i, n)
        return False
