"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            if nums[l] + nums[r] == target:
                return [l + 1, r + 1]
            elif nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
        return [-1, -1]
