"""
https://leetcode.com/problem-list/sliding-window/
url: 
"""


class Solution:
    def longestEqualSubarray(self, nums: list[int], k: int) -> int:
        mx = i = 0
        d = {}
        for j, x in enumerate(nums):
            d[x] = d.get(x, 0) + 1
            mx = max(mx, d[x])
            if j - i + 1 - mx > k:
                d[nums[i]] -= 1
                i += 1
        return mx
