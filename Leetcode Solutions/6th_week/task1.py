"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices/description/
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        count = 0
        ans = 0
        for i in range(len(nums) - 2):
            diff_1 = nums[i + 1] - nums[i]
            diff_2 = nums[i + 2] - nums[i + 1]
            if diff_1 == diff_2:
                count += 1
            else:
                ans += count * (count + 1) // 2
                count = 0

        if count > 0:
            ans += count * (count + 1) // 2

        return ans
