"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/single-number-ii/description/
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twice = 0

        for num in nums:
            ones ^= num & ~twice
            twice ^= num & ~ones

        return ones
