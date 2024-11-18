"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/binary-subarrays-with-sum/description/
"""


class Solution:
    def atMost(self, nums: list[int], goal: int) -> int:
        l, r = 0, 0
        n = len(nums)
        sm = 0
        while l < n and r < n:
            goal -= nums[r]
            while l < n and goal < 0:
                goal += nums[l]
                l += 1
            sm += r - l + 1
            r += 1
        return sm

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        if goal == 0:
            return self.atMost(nums, goal)
        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)
