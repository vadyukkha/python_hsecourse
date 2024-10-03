"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/make-sum-divisible-by-p/description/
"""


class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0
        d = {0: -1}
        cur, mn_len = 0, len(nums)
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            ost = (cur - target) % p
            mn_len = min(mn_len, i - d[ost]) if ost in d else mn_len
            d[cur] = i
        return -1 if mn_len == len(nums) else mn_len
